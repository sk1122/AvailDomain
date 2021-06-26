function check_domain_availabilty(domain, get_all_details) {
	// Check if Domain is Available
	// @params - domain - string
	// @params - get_all_details - boolean
	// API Route - /api/check_domain
	fetch("{% url 'check_availablity' %}", {
		method: 'POST',
		body: JSON.stringify({
			domain: domain
		}),
		headers: {
			'Content-Type': 'application/json',
			"X-CSRFToken": Cookies.get('csrftoken')
		}
	})
	.then(res => {
		const d = res.json()
		.then(data => {
			if(data.data == null) {
				domain_data.innerHTML = `<h1>${domain}</h1><span class="mx-5 btn btn-success">Available</span>`
			} else {
				domain_data.innerHTML = `
					<h1>${data.data['name']}</h1>
					<p>${data.data['registrant_country']} | ${data.data['registrant']}</p>
					<p>Creation Date - ${data.data['creation_date']}</p>
					<p>Expiration Date - ${data.data['expiration_date']}</p>
					<p>Registrar - ${data.data['registrar']}</p>

					<p>Name Servers - ${data.data['name_servers']}</p>
				`
			}
		})
	})
}

function get_available_tlds(sld) {
	// @params - sld - string
	fetch("{% url 'get_available_tlds' %}")
	.then(res => res.json())
	.then(data => {
		available_tlds = data.data
		let sld = domain.value.split(".")[0]
		for(let i = 0; i < available_tlds.length; i++) {
			other_domains.innerHTML += `<p id="${available_tlds[i]}">${sld + available_tlds[i]}</p>`
		}
		check_other_domains(sld)
	})
}
fetch("data/product.json")
    .then(response => response.json())
    .then(data => {
        const productList = document.querySelector("#product-list");
        
        Object.values(data).forEach(product => {
            const productElement = document.createElement("div");
            productElement.classList.add("product");
            
            const tagsHTML = product.categories_tags
                .map(tag => `<li class="tag">${tag}</li>`)
                .join('');
            
            productElement.innerHTML = `
                <img src="${product.image_url}" alt="${product.product_name}">
                <h2>${product.product_name}</h2>
                <p>${product.brands}</p>
                <p>${product.ingredients_text}</p>
                <ul>
                    ${tagsHTML}
                </ul>
            `;
            
            productList.appendChild(productElement);
        });
    })
    .catch(error => console.error('Error loading products:', error));
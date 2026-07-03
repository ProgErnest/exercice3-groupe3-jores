fetch("data/data.json")
    .then(response => response.json())
    .then(data => {
        const productList = document.querySelector("#product-list");
        
        Object.values(data).forEach(product => {
            console.log(product, product!=null);
            if(product != null){
                const productElement = document.createElement("div");
                productElement.classList.add("product");
                
                const tagsHTML = product.categories_tags
                    .map(tag => `<li class="tag">${tag}</li>`)
                    .join('');
                
                productElement.innerHTML = `
                    <img src="${product.image_url ?? 'placeholder-image.png'}" alt="${product.product_name}">
                    <h2>${product.product_name}</h2>
                    <h3>''${product.brands}''</h3>
                    <p>${product.ingredients_text}</p>
                    <div class="tag-container">
                        <ul>
                            ${tagsHTML}
                        </ul>
                    </div
                `;
                productList.appendChild(productElement);

            }else{
                const productElement = document.createElement("div");
                productElement.classList.add("product");
                productElement.innerHTML = `
                    <p>Product not found</p>
                `;
            }
            
        });
    })
    .catch(error => console.error('Error loading products:', error));
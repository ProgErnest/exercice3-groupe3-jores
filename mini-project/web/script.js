fetch("data/product.json")
.then(response => response.json())
.then(data => {
    // console.log(data);
    // data.forEach(product => {
        let i = 0;
        ob = Object.keys(data);
        for (i = 0; i < ob.length; i++) { 
            console.log(i);
            let product = data[i];
            const productElement = document.createElement("div");
            productElement.classList.add("product");
            productElement.innerHTML = `
                <h2>${product.product_name}</h2>
                <p>Brand: ${product.brands}</p>
                <p>Ingredients: ${product.ingredients_text}</p>
                <img src="${product.image_url}" alt="${product.product_name}">
                <p>Categories: ${product.categories_tags}</p>

            `;
            document.body.appendChild(productElement);
        }
    
})

function filterProducts() {
    const checkboxes = document.querySelectorAll('input[type="checkbox"]');
    const selectedCategories = [];

    checkboxes.forEach(checkbox => {
        if (checkbox.checked) {
            selectedCategories.push(checkbox.getAttribute('data-button-name'));
        }
    });

    const products = document.querySelectorAll('.box-item');

    products.forEach(product => {
        const productCategory = product.getAttribute('data-category');
        if (selectedCategories.length === 0 || selectedCategories.includes(productCategory)) {
            product.style.display = 'block';
        } else {
            product.style.display = 'none';
        }
    });
}

function clearAll() {
    const checkboxes = document.querySelectorAll('input[type="checkbox"]');
    checkboxes.forEach(checkbox => {
        checkbox.checked = false;
    });
    filterProducts();
}

function toggleButton(checkbox) {
    const buttonContainer = document.getElementById('button-container');
    const buttonName = checkbox.nextElementSibling.getAttribute('data-name'); // Mengambil nama dari atribut data

    if (checkbox.checked) {
        // Jika checkbox dicentang, buat tombol
        const button = document.createElement('button');
        button.className = 'btn btn-sm btn-dark me-2';
        button.innerText = buttonName; // Set nama tombol
        button.onclick = function() {
            // Aksi ketika tombol diklik
            buttonContainer.removeChild(button); // Menghapus tombol dari kontainer
            checkbox.checked = false; // Mengubah status checkbox menjadi tidak dicentang
        };
        buttonContainer.appendChild(button); // Menambahkan tombol ke kontainer
    } else {
        // Jika checkbox tidak dicentang, hapus tombol yang sesuai
        const buttons = buttonContainer.getElementsByTagName('button');
        for (let i = 0; i < buttons.length; i++) {
            if (buttons[i].innerText === buttonName) {
                buttonContainer.removeChild(buttons[i]);
                break;
            }
        }
    }
}

function clearAll() {
    const buttonContainer = document.getElementById('button-container');
    buttonContainer.innerHTML = ''; // Menghapus semua tombol dari kontainer

    // Mengembalikan semua checkbox ke status tidak dicentang
    const checkboxes = document.querySelectorAll('input[type="checkbox"]');
    checkboxes.forEach(checkbox => {
        checkbox.checked = false;
    });
}
let checkboxes = document.querySelectorAll('.checkbox');
let searchBtn = document.querySelector('.search-btn');

if (searchBtn) {
    searchBtn.addEventListener('click', function(e) {
        if (checkCheckBoxes()) {
            alert('Please select at least one streaming provider.');
            e.preventDefault();
        }
    });
}


const checkCheckBoxes = () => {
    checks = 0
    for (const checkbox of checkboxes) {
        if (checkbox.checked) {
            checks++;
        }
    } 
    if (checks == 0){
        return true;
    }
    return false;
}
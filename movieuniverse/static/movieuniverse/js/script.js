let checkboxes = document.querySelectorAll('.checkbox');
let searchBtn = document.querySelector('.search-btn');
let wrapper = document.querySelector('.loading-wrapper');


if (searchBtn) {
    searchBtn.addEventListener('click', function(e) {
        if (checkCheckBoxes()) {
            alert('Please select at least one streaming provider.');
            e.preventDefault();
        }
    });
}

const load = () =>
{
    wrapper.innerHTML = "Loading..."
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
    else {
        return false;
    }
}
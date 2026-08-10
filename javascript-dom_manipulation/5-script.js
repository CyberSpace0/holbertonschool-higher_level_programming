const updateHeader = document.getElementById('update_header');
const header = document.querySelector('header');
updateHeader.onclick = function() {
	header.textContent = 'New Header!!!';
};

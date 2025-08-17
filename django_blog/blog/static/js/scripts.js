function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let cookie of cookies) {
            cookie = cookie.trim();
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');

fetch("/some-url/", {
    method: "POST",
    headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrftoken
    },
    body: JSON.stringify({ data: "test" })
});
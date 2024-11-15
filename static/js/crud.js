BASE_URL = "http://localhost:3000/api/v1"
MIN_SEARCH_STRING_LENGTH = 2;

sorting_select = document.getElementById("sorting_select")

sorting_select.addEventListener("change", ({target: {value}}) => {
    const [sort_by, sort_order] = value.split(":");
    const newURL = `${window.location.origin}?sort_by=${sort_by}&sort_order=${sort_order}`;

    window.location.href = newURL;
})

let currentController = null

search_container = document.getElementById("search_container")
search_results = document.getElementById("search_results")
search_input = document.getElementById("default-search")
search_input.addEventListener("keyup", async ({ target: { value } }) => {
    search_results.innerHTML = ""

    if (value.length >= MIN_SEARCH_STRING_LENGTH) {
        results = await fetch_search_results(value);
        book_results = results.map(book => create_search_result(book))
        book_results.forEach(book => search_results.appendChild(book))
    }
    else {
        info_string = document.createElement('p');
        info_string.className = "p-4"
        info_string.innerText = `Enter at least ${MIN_SEARCH_STRING_LENGTH} characters to start search.`

        search_results.appendChild(info_string)
    }
})

search_input.addEventListener("focus", (e) => {
    search_container.classList.remove("hidden")
})

search_input.addEventListener("blur", (e) => {
    search_container.classList.add("hidden")
})

async function fetch_search_results(search_query) {
    if (currentController) {
        currentController.abort();
    }

    currentController = new AbortController();
    const signal = currentController.signal;

    return fetch(`${BASE_URL}/books/search?q=${search_query}`, {signal}).then(res => res.json())
}


delete_buttons = document.querySelectorAll("button[data-book-delete]")
delete_buttons.forEach(button => button.addEventListener("click", async (e) => {
        if (confirm(`Do you really want to delete book "${button.dataset.bookTitle}"?`)) {
            try {
                res = await delete_book(button.dataset.bookDelete)
                deleted_book = await res.json()

                location.reload()
                return `Successfully deleted book {deleted_book.id}`
            }
            catch (e) {
                console.error("error: ", e)
            }
        }
    })
)

async function delete_book(book_id) {
    return fetch(`${BASE_URL}/books/${book_id}`, {
        method: "DELETE",
    })
}

function create_search_result(book) {
    const containerDiv = document.createElement('a');
    containerDiv.href = "/asd"
    containerDiv.className = 'flex items-center gap-4 border-b p-4';

    const img = document.createElement('img');
    img.className = 'w-10 h-10 rounded-full object-cover object-center';
    img.src = book.author.image;
    img.alt = 'Author avatar'

    const innerDiv = document.createElement('div')

    const h5 = document.createElement('h5');
    h5.className = 'text-base font-semibold';
    h5.textContent = book.title;

    const span = document.createElement('span');
    span.className = 'bg-blue-100 text-blue-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded dark:bg-blue-900 dark:text-blue-300';
    span.textContent = book.isbn;

    h5.appendChild(span);

    const p = document.createElement('p');
    p.className = 'text-sm text-mute';
    p.textContent = book.author.name;

    innerDiv.appendChild(h5);
    innerDiv.appendChild(p);

    containerDiv.appendChild(img);
    containerDiv.appendChild(innerDiv);

    return containerDiv
}
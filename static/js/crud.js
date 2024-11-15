BASE_URL = "http://localhost:3000/api/v1"

sorting_select = document.getElementById("sorting_select")

sorting_select.addEventListener("change", ({target: {value}}) => {
    const [sort_by, sort_order] = value.split(":");
    const newURL = `${window.location.origin}?sort_by=${sort_by}&sort_order=${sort_order}`;

    window.location.href = newURL;
})

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
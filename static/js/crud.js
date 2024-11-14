BASE_URL = "http://localhost:3000/api/v1"

delete_buttons = document.querySelectorAll("button[data-book-delete]")

delete_buttons.forEach(button => button.addEventListener("click", async (e) => {
        if (confirm(`Do you really want to delete book ${button.dataset.bookDelete}?`)) {
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
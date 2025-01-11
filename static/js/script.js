// Event Listener ensures that the page is loaded before executing function
document.addEventListener('DOMContentLoaded', function () {

    const titleField = document.getElementById("id_title"); // assigns title to titleField
    const slugField = document.getElementById("id_slug"); // assigns slug to slugField
    const nameField = document.getElementById("id_name"); // assigns name to nameField
    const slugAuthorField = document.getElementById("id_slug_author"); //assigns slug_author to slugAuthorField

    // For Book
    if (titleField && slugField) {
        // Event listener listens for the user to input text into the titleField before executing function
        titleField.addEventListener("input", function () {
            // Assigns the value of titleField to slugValue but applies filters so that it is written in slug format
            const slugValue = titleField.value 
                .toLowerCase()
                .trim()
                .replace(/[^a-z0-9\s-]/g, "") // Remove special characters
                .replace(/\s+/g, "-") // Replace spaces with dashes
                .replace(/-+/g, "-"); // Remove multiple consecutive dashes
            slugField.value = slugValue; // assigns the value to the variable
        });
    }

    // For Author
    if (nameField && slugAuthorField) {
        // Event listener listens for the user to input text into the nameField before executing function
        nameField.addEventListener("input", function () {
            // Assigns the value of nameField to slugAuthorValue but applies filters so that it is written in slug format
            const slugAuthorValue = nameField.value
                .toLowerCase()
                .trim()
                .replace(/[^a-z0-9\s-]/g, "") // Remove special characters
                .replace(/\s+/g, "-") // Replace spaces with dashes
                .replace(/-+/g, "-"); // Remove multiple consecutive dashes
            slugAuthorField.value = slugAuthorValue; // assigns the value to the variable
        });
    }
});

// Called by the Delete button to delete Reviews and Authors from the database
function confirmDelete() {
    return confirm("Are you sure you want to delete this content? This action cannot be undone.");
}

document.addEventListener('DOMContentLoaded', function () {
    const titleField = document.getElementById("id_title");
    const slugField = document.getElementById("id_slug");
    const nameField = document.getElementById("id_name");
    const slugAuthorField = document.getElementById("id_slug_author")

    if (titleField && slugField) {
        titleField.addEventListener("input", function () {
            const slugValue = titleField.value
                .toLowerCase()
                .trim()
                .replace(/[^a-z0-9\s-]/g, "") // Remove special characters
                .replace(/\s+/g, "-") // Replace spaces with dashes
                .replace(/-+/g, "-"); // Remove multiple consecutive dashes
            slugField.value = slugValue;
        });
    }
    
    if (nameField && slugAuthorField) {
        nameField.addEventListener("input", function () {
            const slugAuthorValue = nameField.value
                .toLowerCase()
                .trim()
                .replace(/[^a-z0-9\s-]/g, "") // Remove special characters
                .replace(/\s+/g, "-") // Replace spaces with dashes
                .replace(/-+/g, "-"); // Remove multiple consecutive dashes
            slugAuthorField.value = slugAuthorValue;
        });
    }
});

function confirmDelete() {
    return confirm("Are you sure you want to delete this review? This action cannot be undone.");
}
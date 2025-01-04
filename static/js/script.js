document.addEventListener('DOMContentLoaded', function () {
    const titleField = document.getElementById('id_title');
    const slugField = document.getElementById('id_slug');

    if (titleField && slugField) {
        titleField.addEventListener('input', function () {
            const slugValue = titleField.value
                .toLowerCase()
                .trim()
                .replace(/[^a-z0-9\s-]/g, '') // Remove special characters
                .replace(/\s+/g, '-') // Replace spaces with dashes
                .replace(/-+/g, '-'); // Remove multiple consecutive dashes
            slugField.value = slugValue;
        });
    }
});
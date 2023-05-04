document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('search-input');
    const searchForm = document.getElementById('search-form');
    const suggestionsBox = document.getElementById('search-suggestions');

    searchInput.addEventListener('input', function() {
        const query = searchInput.value.trim();

        if (query.length > 2) {
            fetch(`/search_suggestions/?q=${query}`)
                .then(response => response.json())
                .then(data => {
                    console.log(data);  // Add this line to debug the response
                    const suggestions = data.suggestions;
                    suggestionsBox.innerHTML = '';
                    if (data.suggestions.length > 0) {
                        suggestionsBox.style.display = 'block';
                        data.suggestions.forEach(suggestion => {
                            const suggestionItem = document.createElement('div');
                            suggestionItem.textContent = suggestion.title;
                            suggestionItem.addEventListener('click', function() {
                                window.location.href = `/blog_post/${suggestion.id}/`; // Updated line

                            });
                            
                            suggestionsBox.appendChild(suggestionItem);
                        });
                        
                    } else {
                        suggestionsBox.style.display = 'none';
                    }
                });
        } else {
            suggestionsBox.style.display = 'none';
        }
    });

    searchInput.addEventListener('blur', function() {
        setTimeout(() => {
            suggestionsBox.style.display = 'none';
        }, 200);
    });

    searchForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const query = searchInput.value.trim();

        if (query) {
            window.location.href = `/search/?q=${encodeURIComponent(query)}`;
        }
    });
});

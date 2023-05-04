$(document).ready(function () {
    $('#search-input').on('input', function () {
        var query = $(this).val();
        if (query.length > 2) {
            $.getJSON("{% url 'search_suggestions' %}", {q: query}, function (data) {
                var suggestionsHtml = '';
                $.each(data.suggestions, function (index, value) {
                    suggestionsHtml += '<a href="/blog_post/' + value.id + '/">' + value.title + '</a><br>';
                });
                $('#suggestions').html(suggestionsHtml);
            });
        } else {
            $('#suggestions').html('');
        }
    });
});

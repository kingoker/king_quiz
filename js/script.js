// Скрываем все блоки с вопросами, кроме первого
$('.question:not(:first)').hide();

// Находим прогресс бар
var $progressBar = $('#quiz-progress');

// Обработчик события для кнопки Submit
$('.question__button').on('click', function() {
  // Проверяем, был ли выбран ответ на предыдущий вопрос
  var $currentQuestion = $(this).closest('.question');
  
  if ($currentQuestion.length !== 0 || $currentQuestion.find(':radio:checked').length > 0) {

    // Если ответ был выбран на предыдущий вопрос, скрываем его и показываем следующий блок с вопросом
    $currentQuestion.hide().addClass('answered');;
    $currentQuestion.next('.question').show();

    // Обновляем значение прогресс бара
    var progressValue = $('.question.answered').length / $('.question').length * 100;
    $progressBar.attr('value', progressValue);

    // Добавляем ответ на предыдущий вопрос в блок #results
    // var $answer = $currentQuestion.find(':checked, :text').val();
    // $('.result').append('<p>' + $answer + '</p>');

    if ($currentQuestion.next('.question').length === 0) {
        // Если это был последний вопрос, показываем блок с результатами
        $('#quiz-progress').hide();
        $('.result').show();
        $('.quiz__header').text('Осталось только получить подарок:');
    }
  } else {
    // Иначе показываем сообщение об ошибке
    alert('Пожалуйста напишите/выберите ответ что бы продолжить');
  }
});
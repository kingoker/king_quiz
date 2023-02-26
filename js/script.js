// Скрываем все блоки с вопросами, кроме первого
$('.question:not(:first)').hide();

// Обработчик события для кнопки Submit
$('.question__button').on('click', function() {
  // Проверяем, был ли выбран ответ на предыдущий вопрос
  var $currentQuestion = $(this).closest('.question');
  
  if ($currentQuestion.length !== 0 || $currentQuestion.find(':radio:checked').length > 0) {

    // Если ответ был выбран на предыдущий вопрос, скрываем его и показываем следующий блок с вопросом
    $currentQuestion.hide();
    $currentQuestion.next('.question').show();

    // Добавляем ответ на предыдущий вопрос в блок #results
    var $answer = $currentQuestion.find(':checked, :text').val();
    $('.result').append('<p>' + $answer + '</p>');

    if ($currentQuestion.next('.question').length === 0) {
        // Если это был последний вопрос, показываем блок с результатами
        $('.result').show();
        $('.quiz__header').text('Ваши ответы:');
    }
  } else {
    // Иначе показываем сообщение об ошибке
    alert('Пожалуйста напишите/выберите ответ что бы продолжить');
  }
});

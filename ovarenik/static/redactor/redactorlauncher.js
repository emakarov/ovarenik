Suit.$(function(){
  Suit.$('textarea').redactor({
    focus: true,
    imageUpload: '/ru/blog/uploadimagejson/',
    fileUpload: '../demo/scripts/file_upload.php',
    imageGetJson: '/ru/blog/redactorimagejson/'
  });
});
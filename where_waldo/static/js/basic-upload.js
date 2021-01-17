$(function () {

  $(".js-upload-photos").click(function () {
    $("#id_img").click();
  });

  function getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1)) + min;
  }

  $("#id_img").fileupload({
    dataType: 'json',
    sequentialUploads: true,  /* 1. SEND THE FILES ONE BY ONE */
    start: function (e) {  /* 2. WHEN THE UPLOADING PROCESS STARTS, SHOW THE MODAL */
      $("#modal-progress").modal("show");
    },
    stop: function (e) {  /* 3. WHEN THE UPLOADING PROCESS FINALIZE, HIDE THE MODAL */
      $("#modal-progress").modal("hide");
    },
    progressall: function (e, data) {  /* 4. UPDATE THE PROGRESS BAR */
      // let progress = parseInt(data.loaded / data.total * 100, 10);
      let progress = 22;
      let strProgress = progress + "%";
      $(".progress-bar").css({"width": strProgress});
      $(".progress-bar").text(strProgress);

      setTimeout(function () {
        let progress = 51;
        let strProgress = progress + "%";
        $(".progress-bar").css({"width": strProgress});
        $(".progress-bar").text(strProgress);
        $('.uploading-title').text("Finding Waldo...");
      }, 1500);

      setTimeout(function () {
        let progress = 51 + getRandomInt(0, 48);
        let strProgress = progress + "%";
        $(".progress-bar").css({"width": strProgress});
        $(".progress-bar").text(strProgress);
      }, 8000);
    },
    done: function (e, data) {
      if (data.result.is_valid) {
        $('.uploading-title').text("Uploading...");
        let $res = $("#result");
        $res.empty();
        $res.append("<h5>Original</h5>")
        // $("#result").append("<img height='400px' width='600px' src='" + data.result.url + "' alt='no-name'>")
        $res.append("<img class='result-img' src='" + data.result.url + "' alt='no-name'>")
        $res.append("<br>")
        $res.append("<h5>Result</h5>")
        // $("#result").append("<img height='400px' width='600px' src='" + data.result.predicted_url + "' alt='no-name'>")
        $res.append("<img class='result-img' src='" + data.result.predicted_url + "' alt='no-name'>")
      }
    }

  });

});

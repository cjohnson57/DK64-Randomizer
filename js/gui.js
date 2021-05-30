window.onload = load_inital;

function load_inital() {
  brython();
  $("#progressmodal").modal({
    show: false,
    backdrop: "static",
  });
  $("#loading").modal({
    show: true,
    backdrop: "static",
  });
  $("#loading").modal("show");
  setTimeout(function () {
    var savedUserJsonString = getCookie("settings");
    if (savedUserJsonString.length === 0) {
      if (
        document
          .getElementById("blocker_selected")
          .options[0].value.toLowerCase() == "vanilla"
      ) {
        const e = new Event("change");
        element = document.querySelector("#blocker_selected");
        element.dispatchEvent(e);
        element = document.querySelector("#troff_selected");
        element.dispatchEvent(e);
      }
    } else {
      var jsonresp = JSON.parse(savedUserJsonString);
      for (var k in jsonresp) {
        document.getElementsByName(k)[0].value = jsonresp[k];
      }
    }
    progression_clicked();
    $("#loading").modal("hide");
  }, 2000);
}

function progression_clicked() {
  if ($("#randomize_progression")[0].checked) {
    $("#seed").removeAttr("disabled");
    $("#seed_button").removeAttr("disabled");
    $("#unlock_all_kongs").attr("disabled", "disabled");
    $("#unlock_all_kongs").prop("checked", true);
  } else {
    $("#seed").attr("disabled", "disabled");
    $("#seed_button").attr("disabled", "disabled");
    $("#unlock_all_kongs").removeAttr("disabled");
  }
}

function randomizeseed(formdata) {
  return new Promise((resolve, reject) => {
    $("#patchprogress").width("30%");
    $("#progress-text").text("Randomizing seed");
    setTimeout(function () {
      response = randomize_data(formdata);
      setTimeout(function () {
        $("#patchprogress").width("40%");
        $("#progress-text").text("Randomizing complete");
        setTimeout(function () {
          resolve(response);
        }, 1000);
      }, 1000);
    }, 1000);
  });
}

function generate_asm(asm) {
  return new Promise((resolve, reject) => {
    $(function () {
      $("#patchprogress").width("60%");
      $("#progress-text").text("Generating ASM");
      L.execute(
        `
      function convert(code_filename)
          lips = require "lips.init";
          local code = {};
          function codeWriter(key, value)
              function isPointer(value)
                  return type(value) == "number" and value >= 0x80000000 and value < 0x80800000;
              end
              if isPointer(key) then
                  table.insert(code, {key - 0x80000000, value});
              end
          end
          lips(code_filename, codeWriter);
          local formatted_code = "";
          for k,v in pairs(code) do
            local pair_string = "";
            for key, value in pairs(v) do
              if(key == 1)
              then
                pair_string = pair_string .. value .. ":";
              else
                pair_string = pair_string .. value;
              end
            end
            formatted_code = formatted_code .. pair_string .. "\\n";
          end
          window.asmcode = formatted_code;
      end
      convert([[` +
          asm +
          "]])"
      );
      setTimeout(function () {
        $("#patchprogress").width("70%");
        $("#progress-text").text("ASM Generated");
        setTimeout(function () {
          resolve(window.asmcode);
        }, 1000);
      }, 1000);
    });
  });
}

function submitdata(downloadlankyfile) {
  if (downloadlankyfile) {
    downloadlankyfile = document.getElementById("downloadjson").checked
  }
  $("input:disabled, select:disabled").each(function () {
    $(this).removeAttr("disabled");
  });
  if ($("#input-file-rom").val() == "") {
    $("#input-file-rom").select();
  } else {
    form = $("#form").serialize();
    $("#progressmodal").modal("show");
    progression_clicked();

    setTimeout(function () {
      randomizeseed(form).then(function (rando) {
        //downloadToFile(rando, 'settings.asm', 'text/plain');
        if (rando == false) {
          setTimeout(function () {
            $("#patchprogress").addClass("bg-danger");
            $("#patchprogress").width("100%");
            $("#progress-text").text("Failed to successfully generate a seed.");
            setTimeout(function () {
              $("#progressmodal").modal("hide");
              $("#patchprogress").removeClass("bg-danger");
              $("#patchprogress").width("0%");
            }, 5000);
          }, 1000);
        } else {
          generate_asm(rando).then(function (binary_data) {
            applyPatch(patch, romFile, false, binary_data);
          });
        }
      });
    }, 1000);
    JSONData = JSON.parse(queryStringToJSON(form));
    if (downloadlankyfile) {
      downloadToFile(JSON.stringify(JSONData), 'dk64r-settings-'+JSONData["seed"]+'.lanky', 'text/plain');
    }
    delete JSONData["seed"];
    setCookie("settings", JSON.stringify(JSONData), 30);
  }
}
function loadlankyfile() {
  $("input:disabled, select:disabled").each(function () {
    $(this).removeAttr("disabled");
  });
  if ($("#input-file-rom").val() == "") {
    $("#input-file-rom").select();
  } else if ($("#jsonfileloader").val() == "") {
    $("#jsonfileloader").select();
  } else {
    var file_hook = document.getElementById("jsonfileloader")
    var fr = new FileReader();
    fr.onload = function() {
      submitlankyfile(JSON.parse(fr.result));
    };
    fr.readAsText(file_hook.files[0]);
  }
}

var file_hook = document.getElementById("jsonfileloader")
file_hook.addEventListener("change", function() {
  var fr = new FileReader();
  fr.onload = function() {
    for (var k in JSON.parse(fr.result)) {
      document.getElementsByName(k)[0].value = JSON.parse(fr.result)[k];
    }
  };
  fr.readAsText(file_hook.files[0]);
})

function submitlankyfile(json_data) {
  console.log(json_data)
  for (var k in json_data) {
    document.getElementsByName(k)[0].value = json_data[k];
  }
  var qs = ""
  submitdata(false)
}

const downloadToFile = (content, filename, contentType) => {
  const a = document.createElement("a");
  const file = new Blob([content], {type: contentType});
  a.href = URL.createObjectURL(file)
  a.download = filename
  a.click();
  URL.revokeObjectURL(a.href);
}

function queryStringToJSON(qs) {
  qs = qs || location.search.slice(1);

  var pairs = qs.split("&");
  var result = {};
  pairs.forEach(function (p) {
    var pair = p.split("=");
    var key = pair[0];
    var value = decodeURIComponent(pair[1] || "");

    if (result[key]) {
      if (Object.prototype.toString.call(result[key]) === "[object Array]") {
        result[key].push(value);
      } else {
        result[key] = [result[key], value];
      }
    } else {
      result[key] = value;
    }
  });
  return JSON.stringify(result);
}

function getCookie(cname) {
  var name = cname + "=";
  var decodedCookie = decodeURIComponent(document.cookie);
  var ca = decodedCookie.split(";");
  for (var i = 0; i < ca.length; i++) {
    var c = ca[i];
    while (c.charAt(0) == " ") {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}

function setCookie(cname, cvalue, exdays) {
  var d = new Date();
  d.setTime(d.getTime() + exdays * 24 * 60 * 60 * 1000);
  var expires = "expires=" + d.toUTCString();
  document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}

var load_selectors = document.getElementsByClassName("load_selector");
const selection_data = [
  {
    "click_id": "selector_newseed",
    "show_ids": [
      "generateseed",
      "downloadsettings"
    ]
  },
  {
    "click_id": "selector_patchfile",
    "show_ids": [
      "loadjsonfile",
      "jsonfileloader",
      "formbreak"
    ]
  }
]
for (var i = 0; i < load_selectors.length; i++) {
    load_selectors[i].addEventListener("click", (evt) => {
        var _load_selectors = document.getElementsByClassName("load_selector")
        for (var j = 0; j < _load_selectors.length; j++) {
            _load_selectors[j].classList.remove("load_selected")
        }
        evt.target.classList.add("load_selected");
        const evt_id = evt.target.getAttribute("id")
        const evt_foundshow = selection_data.find(item => item.click_id == evt_id)
        const evt_foundhide = selection_data.filter(item => item.click_id != evt_id)
        if (evt_foundshow) {
          evt_foundshow.show_ids.forEach(item => {
            document.getElementById(item).classList.remove("hide")
          })
        }
        evt_foundhide.forEach(item => {
          item.show_ids.forEach(item2 => {
            document.getElementById(item2).classList.add("hide")
          })
        })
    }, false)
}
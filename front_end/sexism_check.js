//BasicIoLayout.config({
  //  sampleLink: "samples.json",
   // submitFunction: submit
//});

function test1(){
    document.getElementById('input-submit').value="She is great at cooking and cleaning.";
}

function test2(){
    document.getElementById('input-submit').value="Women are great at cooking and cleaning.";
}

function test3(){
    document.getElementById('input-submit').value="I bought some sausage from the supermarket today.";
}

function test4(){
    document.getElementById('input-submit').value="Do you like eating sausage?";
}

function test5(){
    document.getElementById('input-submit').value="Rapists must be in jail.";
}

function test6(){
    document.getElementById('input-submit').value="This dress attracts rapists.";
}




function submit() {
    document.getElementById("btn-submit").className += " disabled";
    var input = document.getElementById('input-submit').value;
    if (input == "") {var input = "Please enter a sentence or choose one of the samples."} ;
    if (input != ""){
      var url = "http://0.0.0.0:1313/"+input;
      url = new URL(url);
      let jsondata;    
      fetch(url).then(function(u){ return u.json();}).then(
        function(json){
            jsondata = json;
            answer = "~~~ This text is "+ jsondata+"% sexist ~~~"
            if (input == "Please enter a sentence or choose one of the samples.") {var answer = ""} ;
            document.getElementById('input-submit').value="";
            document.getElementById('result42').innerHTML=answer;
            document.getElementById('input-submit').placeholder=input;
            document.getElementById("btn-submit").className = "aix-button button button--primary button--full";
        }
      )
    };
}

function formatAnswer(input) {
    input = JSON.parse(input);
    return ('<p>' + input + '</p>');

}

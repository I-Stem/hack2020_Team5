var app=angular.module("myApp",[]);
  app.controller('myCtrl', function($scope, $http) {
	   $('#capture2').hide();
	    $('#read2').hide();
	  $("#files2").hide();
		$('#last').hide();


	$scope.filesave=function(mytext){
		$scope.text={};
		$scope.text.mypdf=mytext
        $http({
                url:'http://172.16.101.103:5001/pdfread',
                dataType:'json',
                method:'POST',
				data:$scope.text,
                headers: {
                            "Content-Type":"application/json"
                }
                }).then(function(resp){
                	console.log(resp.data.message);
				$("#files2").hide();
					$("#last").show();
				})

      }

	$scope.imgread=function(){
        $http({
                url:'http://172.16.101.103:5001/imgread',
                dataType:'json',
                method:'POST',
                headers: {
                            "Content-Type":"application/json"
                }
                }).then(function(resp){
                    console.log(resp.data.message);
                $("#capture2").hide();
                    $("#last").show();
                })

      }

	$scope.uploadfunc=function(){
                var filepath = (document.getElementById("myFile")).files[0];
                var formData = new FormData();
                formData.append("file",filepath);


                var request = new XMLHttpRequest();
                request.open("POST","http://172.16.101.103:5001/filesave");
                request.send(formData);
                request.onreadystatechange = function(){
                    if(request.readyState == 4 && request.status == 200)
                    {
                            var text = "File uploaded Successfully"

                            var msg = new SpeechSynthesisUtterance();
                            var voices = window.speechSynthesis.getVoices();
                            msg.voice = voices[1];
                            msg.rate = 2;
                            msg.pitch = 1;
                            msg.text = text;

                            speechSynthesis.speak(msg);
							console.log(request.response);
							$scope.filesave(request.response);
                    }
                }
            }
	  $scope.summary=function(){
	  	$http({
				url:'http://172.16.101.103:5001/summary',
				dataType:'json',
			    method:'POST',
				headers: {
							"Content-Type":"application/json"
				}
				}).then(function(resp){
					var text = resp.data.message;
                  var msg = new SpeechSynthesisUtterance();
                  var voices = window.speechSynthesis.getVoices();
                  msg.voice = voices[1];
                  msg.rate = 2;
                  msg.pitch = 1;
                  msg.text = text;


                  speechSynthesis.speak(msg);
				})

	  }

	  
		$scope.read=function(){
        $http({
                url:'http://172.16.101.103:5001/readentire',
                dataType:'json',
                method:'POST',
                headers: {
                            "Content-Type":"application/json"
				}
				}).then(function(resp){
                    var text = resp.data.message;
                  var msg = new SpeechSynthesisUtterance();
                  var voices = window.speechSynthesis.getVoices();
                  msg.voice = voices[1];
                  msg.rate = 2;
                  msg.pitch = 1;
                  msg.text = text;


                  speechSynthesis.speak(msg);
                })

      }


			$scope.keyword=function(){
        $http({
                url:'http://172.16.101.103:5001/keyword',
                dataType:'json',
                method:'POST',
                headers: {
                            "Content-Type":"application/json"
				}
				}).then(function(resp){
                    var text = resp.data.message;
                  var msg = new SpeechSynthesisUtterance();
                  var voices = window.speechSynthesis.getVoices();
                  msg.voice = voices[1];
                  msg.rate = 2;
                  msg.pitch = 1;
                  msg.text = text;


                  speechSynthesis.speak(msg);
                })

      }

	$(function(){
		  if ('speechSynthesis' in window) {
			
			$('#capture').click(function(){
				  var text = "You have selected capturing from mobile camera, please double click to preoceed";
				  var msg = new SpeechSynthesisUtterance();
				  var voices = window.speechSynthesis.getVoices();
				  msg.voice = voices[1];
				  msg.rate = 2;
				  msg.pitch = 1;
				  msg.text = text;

				 
				  speechSynthesis.speak(msg);
				  $('#capture').hide();
				  $('#read').hide();
				  $('#read2').hide();
				  $('#capture2').show();
				})
				
			$('#capture2').dblclick(function(){
				  var text = "Please open IP Webcam";
				  var msg = new SpeechSynthesisUtterance();
				  var voices = window.speechSynthesis.getVoices();
				  msg.voice = voices[1];
				  msg.rate = 2;
				  msg.pitch = 1;
				  msg.text = text;

				 
				  speechSynthesis.speak(msg);
				  $('#capture2').hide();
				  $('#last').show();
				})	
				
				
			$('#read').click(function(){
				  var text = "You have chosen the option to read from PDF, Please double click to proceed";
				  var msg = new SpeechSynthesisUtterance();
				  var voices = window.speechSynthesis.getVoices();
				  msg.voice = voices[1];
				  msg.rate = 2;
				  msg.pitch = 1;
				  msg.text = text;

				 
				  speechSynthesis.speak(msg);
				  $('#read').hide();
				  $('#capture').hide();
				  $('#capture2').hide();	
				  $('#read2').show();
				})
				
			$('#read2').dblclick(function(){
				  var text = "Please select file to upload";
				  var msg = new SpeechSynthesisUtterance();
				  var voices = window.speechSynthesis.getVoices();
				  msg.voice = voices[1];
				  msg.rate = 2;
				  msg.pitch = 1;
				  msg.text = text;

				 
				  speechSynthesis.speak(msg);
				  //$('#read').hide();

				  $('#read2').hide();
				  $("#files2").show();

				})		
			  $('#files2').dblclick(function(){
				$scope.uploadfunc();
                })


			  $('#last').dblclick(function(){

                  $('#capture2').hide();
				  $('#last').hide();
				  $('#read2').hide();
                  $("#files2").hide();
			 	  $('#capture').show();
				  $('#read').show();
                })
				
			  } 
			  
			 else {
				var text = "Speech to text is not supported";
				  var msg = new SpeechSynthesisUtterance();
				  //var voices = window.speechSynthesis.getVoices();
				  //msg.voice = voices[$('#voices').val()];
				  msg.rate = 1;
				  msg.pitch = 2;
				  msg.text = text;

				 
				  speechSynthesis.speak(msg);
			  }
		});

  });

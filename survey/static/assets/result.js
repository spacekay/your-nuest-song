function likeResult(rid) {
                url = "/like/"+rid
                fetch(url).then(response => {
                   if(response.ok) {
                       alert("결과 선호도 등록을 완료하였습니다.")
                       return true;
                   } else {
                       alert("결과 선호도는 한 번만 등록 가능합니다.")
                       return false;
                   }
                });
            }

            function dislikeResult(rid) {
                url = "/dislike/"+rid
                fetch(url).then(response => {
                   if(response.ok) {
                       alert("결과 선호도 등록을 완료하였습니다.")
                       return true;
                   } else {
                       alert("결과 선호도는 한 번만 등록 가능합니다.")
                       return false;
                   }
                });
            }
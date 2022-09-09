$(document).ready(function() {
    $('.button_question').on("click", function () {

        let id = $('.question_id').attr('id')
        let answer = ''
        let last = 'last'
        if ($(this).attr('id') === 'yes'){
            answer = 1
        }
        else if ($(this).attr('id') === 'no'){
            answer = 0
        }

        if ((String(id) === '6') && (String(answer) === '1')) {
            let result = 'Человек-человек'
            $.ajax({
               url: '/result/',
               data: {'res':result},
               method: 'POST',
                success: function (){
                   window.location.href = 'http://127.0.0.1:8000/ege/'
                }
            });
        }
        else if ((String(id) === '7') && (String(answer) === '1')) {
            let result = 'Человек-природа'
            $.ajax({
               url: '/result/',
               data: {'res':result},
               method: 'POST',
                success: function (){
                   window.location.href = 'http://127.0.0.1:8000/ege/'
                }
            });
        }
        else if ((String(id) === '11') && (String(answer) === '1')) {
            let result = 'Человек-техника'
            $.ajax({
               url: '/result/',
               data: {'res':result},
               method: 'POST',
                success: function (){
                   window.location.href = 'http://127.0.0.1:8000/ege/'
                }
            });
        }
        else if ((String(id) === '21') && (String(answer) === '1')) {
            let result = 'Человек-знаковая система'
            $.ajax({
               url: '/result/',
               data: {'res':result},
               method: 'POST',
                success: function (){
                   window.location.href = 'http://127.0.0.1:8000/ege/'
                }
            });
        }
        else if ((String(id) === '22') && (String(answer) === '0')) {
            let result = 'Человек-?'
            $.ajax({
               url: '/result/',
               data: {'res':result},
               method: 'POST',
                success: function (){
                   window.location.href = 'http://127.0.0.1:8000/ege/'
                }
            });
        }
        else if ((String(id) === '23') && (String(answer) === '0')) {
            let result = 'Человек-?'
            $.ajax({
               url: '/result/',
               data: {'res':result},
               method: 'POST',
                success: function (){
                   window.location.href = 'http://127.0.0.1:8000/ege/'
                }
            });
        }
        else if ((String(id) === '24') && (String(answer) === '0')) {
            let result = 'Человек-?'
            $.ajax({
               url: '/result/',
               data: {'res':result},
               method: 'POST',
                success: function (){
                   window.location.href = 'http://127.0.0.1:8000/ege/'
                }
            });
        }
        else if ((String(id) === '25') && (String(answer) === '0')) {
            let result = 'Человек-?'
            $.ajax({
               url: '/result/',
               data: {'res':result},
               method: 'POST',
                success: function (){
                   window.location.href = 'http://127.0.0.1:8000/ege/'
                }
            });
        }
        else if ((String(id) === '25') && (String(answer) === '1')) {
            let result = 'Человек-художественный образ'
            $.ajax({
               url: '/result/',
               data: {'res':result},
               method: 'POST',
                success: function (){
                   window.location.href = 'http://127.0.0.1:8000/ege/'
                }
            });
        }

        else{
            $.ajax({
                method: "GET",
                data: { id: id, answer: answer },
                url: "ans/",
                success: function (data){

                    datas = data['data']
                    if ( typeof(datas !== 'undefined' && datas !== null )) {
                        $('#question_title').text(datas['text'])
                        $('.question_id').attr('id', datas['id'])
                    }
                    else{
                        document.innerHTML = data
                    }

                }
            });
        }
    });

    let itogob = 0;
    let valid = 0;


    function validsend(input){
        if ($(input).val()>0){
            itogob++
            if ($(input).val() > 10){
                valid++
            }
        }
    }
    function validbal(input){
        if ($(input).val()>0){
            if ($(input).val() > 10){
                $(input).addClass('is-valid')
                $(input).removeClass('is-invalid')
            }
            else{
                $(input).addClass('is-invalid')
                $(input).removeClass('is-valid')
            }
        }

    }

    let rus = $(document).find('.predbal')[0]
    let mat = $(document).find('.predbal')[1]
    let fiz = $(document).find('.predbal')[2]
    let him = $(document).find('.predbal')[3]
    let ist = $(document).find('.predbal')[4]
    let obsh = $(document).find('.predbal')[5]
    let ikt = $(document).find('.predbal')[6]
    let bio = $(document).find('.predbal')[7]
    let geo = $(document).find('.predbal')[8]
    let ang = $(document).find('.predbal')[9]
    let lit = $(document).find('.predbal')[10]
    rus.oninput = function (){
         validbal(this)
    }
    mat.oninput = function (){
         validbal(this)
    }
    fiz.oninput = function (){
         validbal(this)
    }
    him.oninput = function (){
         validbal(this)
    }
    ist.oninput = function (){
         validbal(this)
    }
    obsh.oninput = function (){
         validbal(this)
    }
    ikt.oninput = function (){
         validbal(this)
    }
    bio.oninput = function (){
         validbal(this)
    }
    geo.oninput = function (){
         validbal(this)
    }
    ang.oninput = function (){
         validbal(this)
    }
    lit.oninput = function (){
         validbal(this)
    }



    $('#itog').on('click', function (){
        $.each($(document).find('.predbal'),function (){

            validsend(this)

        })
        console.log(itogob)
        console.log(valid)

        if (itogob === valid && (valid >= 3)){


        let data = []

        $.each(document.getElementsByClassName('bal'), function (){
           let names = this.getElementsByTagName('label')[0].innerText
           let bal = this.getElementsByTagName('input')[0].value
            if (bal !== ''){
                 data.push(names+' '+bal)
            }
        });
        console.log(data)

        $.ajax({
                method: "POST",
                data: {'datas':data},
                url: "/info/",
                success: function (data){
                    console.log(data['data'])
                    $('.balli').hide()
                    $('.result').show()

                    data = data['data']
                    $.each(data,function (){
                        console.log(this)

                        $('.result').append('<div className="card"> <div class="card-header"> <h1> Направление: '+ this['Направление'] +
                            '</h1> <h2> Профильный предмет: '+ this['Профильный предмет']+'</h2> <h3> Институт: '+ this['Институт']+
                            '</h3> <span> Возможные профессии: '+ this['Профессии']+'</span> ' +
                            '<h2 style="color: green"> Средний предполагаемый балл:'+this['Вероятность балла']+ '</h2>' +
                            '<h2 style="color: orange"> Ваш средний балл:'+this['Сб']+'</h2>' +
                            '<h2 style="color: red"> Точность прогноза: '+this['Тп']+'%</h2> </div> </div>' )
                    })

                }
        });
        }
        itogob = 0;
            valid = 0;
    });

});
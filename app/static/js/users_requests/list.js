import {showMessage, PROTOCOL, ENDPOINT} from './utils.js'


$('document').ready(function () {
    var users_container = $("#users_container");
    users_container.html("<h2>Loading users...</h2>");
    $("#page-size").on("change", function () {
        changePageSize();
    });
});

$(function () {
    (function (name) {
        var container = $('#pagination-' + name);
        var sources = function () {
            var result = [];

            for (var i = 1; i < 196; i++) {
                result.push(i);
            }

            return result;
        }();
        var page_size = $("#page-size").val();
        var options = {
            dataSource: PROTOCOL + ENDPOINT + 'users',
            locator: 'users',
            totalNumberLocator: function (response) {
                return response.total
            },
            pageSize: page_size,
            alias: {
                pageNumber: 'page',
                pageSize: 'page_size'
            },
            className: 'paginationjs-theme-blue paginationjs-big',
            callback: function (response, pagination) {
                if (response.length === 0){
                    withoutUsers();
                }else {
                    renderUsers(response, response.length, pagination.totalNumber)
                }
            }
        };

        container.pagination(options);

        container.addHook('afterPageOnClick', function () {
            showMessage('Success', 'Users loaded successfully');
            goTopPage();
        });
    })('users');


})

function renderUsers(data, users_number, total) {
    var users_container = $("#users_container");
    users_container.empty();
    var cards = "";
    for (let i = 0; i < users_number; i++) {
        cards = `<div class="col-sm-3 mb-4"><div class="card" id="nota_card-${data['username']}">
                        <div class="card-header info-card">
                            <a target="_blank" href="${data[i]['profile_url']}">${data[i]['username']}</a>
                        </div>
                        <img class="card-img-top" src="${data[i]['image_url']}" alt="${data[i]['username']}">
                        <div class="card-body">
                        </div>
                        <div class="card-footer">
                          <small class="text-muted">Type: ${data[i]['type']}</small>
                        </div>
                    </div></div>`
        users_container.append(cards).hide().fadeIn(500);
    }
    $("#total_users").html(total)

}

function changePageSize() {
    var container = $('#pagination-users');
    var page_size = $("#page-size").val();

    var options = {
        dataSource: PROTOCOL + ENDPOINT + 'users',
        locator: 'users',
        totalNumberLocator: function (response) {
                return response.total
            },
        pageSize: page_size,
        alias: {
            pageNumber: 'page',
            pageSize: 'page_size'
        },
        className: 'paginationjs-theme-blue paginationjs-big',
        callback: function (response, pagination) {
            renderUsers(response, response.length, pagination.totalNumber)
        }
    };

    container.pagination(options);

    container.addHook('afterPageOnClick', function () {
        showMessage('Success', 'Users loaded successfully');
        goTopPage();
    });

}

function goTopPage() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}

function withoutUsers(){
    var users_container = $("#users_container");
    users_container.html("<h2>No users were found :(</h2>");
    $("#pagination-users").empty();
}

function generateUUID() {
    var d = new Date().getTime();
    if (window.performance && typeof window.performance.now === 'function') {
        d += performance.now(); //use high-precision timer if available
    }
    var uuid = 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g,
        function(c) {
            var r = (d + Math.random() * 16) % 16 | 0;
            d = Math.floor(d / 16);
            return (c == 'x' ? r : (r & 0x3 | 0x8)).toString(16);
        });
    return uuid;
}

function formatDate(value) {//调用时间戳为日期显示
    let date = new Date(value);
    let y = date.getFullYear();  //获取年份
    let month = date.getMonth() + 1;  //获取月份
    month = month < 10 ? '0' + month : month;  //月份不满10天显示前加0
    let d = date.getDate();  //获取日期
    d = d < 10 ? '0' + d : d;  //日期不满10天显示前加0

    //也可以获取更精准时间
    let h = date.getHours();                   //小时
    let m = date.getMinutes();                 //分
    let s = date.getSeconds();                 //秒
    return y + '-' + month + '-' + d + ' ' + h + ':' + m + ':' + s;
    //let ls = date.getMilliseconds()            //毫秒
}

function parseData(res) { // res 即为原始返回的数据
    return {
        'code': res.meta.status === 'success' ? 0 : 1, //解析接口状态
        'msg': res.meta.message, //解析提示文本
        'data': res.result.department_list, //解析数据列表
    };
}

/**封装请求接口**/
async function request(method, url, data = {}) {
    const options = {
        method: method,
        headers: {
            'Content-Type': 'application/json',
            // 'Authorization': `Bearer ${localStorage.getItem('jwt')}`,
        },
        body: JSON.stringify(data),
    };
    const response = await fetch(url, options);
    return await response.json();
}

async function get_api(url, data) {
    return request('GET', url, data);
}

async function post_api(url, data) {
    return request('POST', url, data);
}

async function put_api(url, data) {
    return request('PUT', url, data);
}

async function delete_api(url, data) {
    return request('DELETE', url, data);
}

async function logout() {
    let option = {
        'method': 'POST',
    };
    return await post_api('/api/private/v1/logout', option);
}

async function login(data) {
    let result = await post_api('/api/private/v1/login', data)
    return await result;
}

async function create_user(data) {
    return post_api(`/api/private/v1/user/`, data);
}

async function remove_user(uid) {
    return await delete_api(`/api/private/v1/user/${uid}`);
}

async function update_user(uid, data) {
    return await put_api(`/api/private/v1/user/${uid}`, data);
}

async function batch_remove_department(data) {
    return await delete_api(`/api/private/v1/department/batch_remove`, data);
}

async function create_department(data) {
    return await post_api(`/api/private/v1/department/`, data);
}

async function remove_department(did) {
    return await delete_api(`/api/private/v1/department/${did}`);
}

async function update_department(did, data) {
    return put_api(`/api/private/v1/department/${did}`, data);
}

async function create_permission(data) {
    return await post_api(`/api/private/v1/permission/`, data);
}

async function remove_permission(pid) {
    return await delete_api(`/api/private/v1/permission/${pid}`);
}

async function update_permission(pid, data) {
    return await put_api(`/api/private/v1/permission/${pid}`, data);
}

async function enable_permission(pid, data) {
    return await put_api(`/api/private/v1/permission/${pid}/enable`, data);
}

async function create_role(data) {
    return await post_api(`/api/private/v1/role/`, data);
}

async function remove_role(rid) {
    return await delete_api(`/api/private/v1/role/${rid}`);
}

async function update_role(rid, data) {
    return await put_api(`/api/private/v1/role/${rid}`, data);
}
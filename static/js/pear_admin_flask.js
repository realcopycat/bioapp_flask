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

async function logout() {
  const options = {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      // 'Authorization': `Bearer ${localStorage.getItem('jwt')}`,
    },
    body: JSON.stringify({}),
  };
  const response = await fetch('/api/private/v1/logout', options);
  return await response.json();
}

async function login(data) {
  const response = await fetch('/api/private/v1/login', {
    method: 'post',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
  });
  return await response.json();
}

async function remove_user(uid) {
  const options = {
    method: 'DELETE',
    headers: {
      'Content-Type': 'application/json',
    },
  };
  const response = await fetch(`/api/private/v1/user/${uid}`, options);
  return await response.json();
}

async function add_user(data) {
  const options = {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${localStorage.getItem('jwt')}`,
    },
    body: JSON.stringify(data),
  };
  const response = await fetch(`/api/private/v1/user/`, options);
  return await response.json();
}

async function edit_user(uid, data) {
  const options = {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${localStorage.getItem('jwt')}`,
    },
    body: JSON.stringify(data),
  };
  const response = await fetch(`/api/private/v1/user/${uid}`, options);
  return await response.json();
}

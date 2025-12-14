
$(() => {
	// 登录注册界面切换事件
	$('.enroll-a').click(() => {
		$('.login').hide();
		$('.enroll').show();
	})
	$('.login-b').click(() => {handoff()})
	const handoff = () => {
		$('.login').show();
		$('.enroll').hide();
	}
 
	// 判断登录账号与密码是否正确事件
	$('.login-a').click(() => {
		const name = $('#name').val();
		const pwd = $('#pwd').val();
		let account = localStorage.getItem('account');
		let password = localStorage.getItem('password');
		if (!name || !pwd) {
			alert('账号或密码不能为空！！！');
		} else if (name == account && pwd == password || name == 666 && pwd == 888) { // 666与888是默认登录账号与密码（可修改或删除）
			alert('登录成功！');
			localStorage.setItem('captcha', 1);
			$('.login').hide();
			// indexbox.html 是登录成功后显示的页面路径（可修改）
			$('body').append('<iframe src="indexbox.html"></iframe>');
		} else {
			alert('账号或密码错误！！！');
		}
	})
 
	// 注册事件储存账号与密码数据
	$('.enroll-b').click(() => {
		const name1 = $('#name1').val();
		const pwd1 = $('#pwd1').val();
		if (!name1 || !pwd1) {
			alert('账号与密码不能为空！！！');
		} else {
			localStorage.setItem('account', name1);
			localStorage.setItem('password', pwd1);
			alert('注册成功！');
			handoff();
			$('#name').val(name1);
			$('#pwd').val(pwd1);
		}
	})
	
	// 判断以前是否登录过，如果是就免登录( 20 表示用户免登录20次就要登录一次 （可修改）)
	const detect = () => {
		if (localStorage.getItem('captcha').length <= 20) {
			const recording = localStorage.getItem('captcha') + 1;
			localStorage.setItem('captcha', recording);
			$('.login').hide();
			// indexbox.html 是登录成功后显示的页面路径（可修改）
			$('body').append('<iframe src="indexbox.html"></iframe>');
		}
	}
	detect();
})

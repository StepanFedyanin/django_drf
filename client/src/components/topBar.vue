<template>
	<div class="topbar">
    <button class="topbar__burger" @click="changeShowMenu(true)">
      <span></span>
    </button>
		<div class="topbar__notifications active">
		</div>
		<div :class="['topbar__menu', showMenu?'active':null]">
			<div class="topbar__head">
				<p class="topbar__title h2">
					Настройки
				</p>
				<button class="topbar__burger topbar__close active" @click="changeShowMenu(false)">
					<span></span>
				</button>
			</div>
			<ul class="topbar__list">
				<li v-for="item in menuList" :key="item.link" :class="['topbar__item', item.icon]">{{item.title}}</li>
			</ul>
      <div class="topbar__feedback q-mt-lg">
        О нас
        <div class="topbar__tools">
          <button class="btn">
            Написать нам
          </button>
          <a class="btn">Позвонить нам</a>
        </div>
      </div>
		</div>
	</div>
</template>

<script>
export default {
	name: 'topbar',
	data() {
		return {
      showMenu: false,
			menuList: [
				{
					icon: 'main',
					link: 'main',
					title: 'Главная'
				},
				{
					icon: 'profile',
					link: 'profile',
					title: 'Профиль'
				},
				{
					icon: 'orders',
					link: 'orders',
					title: 'Мои заказы'
				}
			]
		}
	},
  methods:{
    changeShowMenu (value) {
      this.showMenu = value;
    }
  }
}
</script>

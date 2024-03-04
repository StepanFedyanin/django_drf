<template>
	<div class="wrapper auth">
		<div class="h1 auth__title">
			Авторизация
		</div>
		<template v-if="template === 'login'">
			<div class="auth__content">
				<div :class="['auth__steps',loginStep === 'sent' ? 'active': null]">
					<q-form class="auth__step" @submit.prevent="sendLogin">
						<q-input
							label="Номер телефона"
							rounded
							outlined
							mask="7 ### ###-##-##"
							v-model="loginFormData.phone"
							placeholder="8 (999) 999 - 99 - 99"
							color="primary"
						/>
						<loader class="auth__next" :show="loaderSendLogin">
							<button class="auth__next--btn btn" :disabled="loaderSendLogin"></button>
						</loader>
					</q-form>
					<q-form class="auth__step" @submit="sendCode">
						<div class="auth__code form__control">
							<label class="form__label">Код из СМС</label>
							<div class="auth__code--control">
								<input
									v-for="code in 6"
									:key="`code_symbol_${code}`"
									class="form__input h2"
									maxlength="1"
									v-model="loginFormData.code[code - 1]"
									type="text"
								/>
							</div>
						</div>
						<q-btn
							color="primary"
							rounded
							type="submit"
							:loading="loaderSendCode"
						>
							Отправить
						</q-btn>
					</q-form>
				</div>
			</div>
		</template>
		<template v-if="template === 'register'">
			<div class="auth__content">
				<div :class="['auth__steps',registerStep === 'valid' ? 'active': null]">
					<form class="auth__step" @submit.prevent="changeStepRegister('valid')">
						<ui-input
							placeholder="8 (999) 999 - 99 - 99"
							maska="7 ### ###-##-##"
							v-model="registerFormData.phone"
							label="Телефон"
							:required="true"
						/>
						<ui-input
							placeholder="example@mail.ru"
							v-model="registerFormData.email"
							label="Почта"
							:required="true"
						/>
						<button class="auth__next auth__next--btn btn"></button>
					</form>
					<form class="auth__step" @submit.prevent="createUser()">
						<ui-input
							v-model="registerFormData.first_name"
							label="Имя"
							placeholder="Сергей"
							:required="true"
						/>
						<ui-input
							v-model="registerFormData.last_name"
							label="Фамилия"
							placeholder="Иванов"
						/>
						<ui-input
							maska="##.##.####"
							v-model="registerFormData.birth_date"
							label="Дата рождения"
							placeholder="13.08.2016"
							:required="true"
						/>
						<loader :show="loaderCreateUser">
							<button class="auth__submit btn">Зарегистрироваться</button>
						</loader>
					</form>
				</div>
			</div>
		</template>
		<div class="auth__footnote ">
			<router-link v-if="template === 'login'" class="p" :to="{name: 'register', params: {template:'register'} }">
				Зарегестрироваться ?
			</router-link>
			<router-link v-if="template === 'register'" class="p" :to="{name: 'login', params: {template:'login'} }">
				Авторизоваться ?
			</router-link>
		</div>
	</div>
</template>

<script>
import {app} from '@/services'
import Loader from "components/UI/loader.vue";

export default {
	name: 'auth',
	components: {Loader},
	data() {
		return {
			loginStep: null,
			registerStep: null,
			loaderSendLogin: false,
			loaderSendCode: false,
			loaderCreateUser: false,
			loginFormData: {
				phone: '',
				code: []
			},
			registerFormData: {
				first_name: '',
				last_name: '',
				phone: '',
				email: '',
				birth_date: ''
			}
		}
	},
	created() {
		console.log(this.$route.props)
	},
	props: {
		template: {
			type: String,
			default() {
				return 'login'
			}
		}
	},
	watch: {
		'loginFormData.code.join()': {
			immediate: true,
			handler(to, from) {
				console.log(to, from)
			},
		},
	},
	methods: {
		sendLogin() {
			this.loaderSendLogin = true;
			const params = {phone: this.loginFormData.phone.replace(/ /g, '').replace(/-/g, '')}
			app.sendPhoneLogin(params).then(data => {
				this.loginStep = data.code;
				this.loaderSendLogin = false;
			}).catch((err) => {
				this.loaderSendLogin = false;
				console.log(err)
			})
		},
		sendCode() {
			this.loaderSendCode = true;
			const params = {
				code: this.loginFormData.code.join(''),
				phone: this.loginFormData.phone.replace(/ /g, '').replace(/-/g, '')
			}
			app.sendCodeLogin(params).then(data => {
				this.$store.dispatch('setToken', data);
				this.loaderSendCode = false;
				this.next('restaurant', {id: 1})
			}).catch((err) => {
				this.loaderSendCode = false;
				console.log(err)
			})
		},
		changeStepRegister(value) {
			this.registerStep = value;
		},
		createUser() {
			this.loaderCreateUser = true;
			setTimeout(() => {
				this.loaderCreateUser = false;
			}, 700)
		},
		next(name, params = {}) {
			this.$router.push({name, params});
		},
	}
}
</script>

<template>
  <div class="container-fluid">
    <div class="row flex-nowrap">
      <div class="col-auto col-md-3 col-xl-2 px-sm-2 px-0 bg-dark">
        <div class="d-flex flex-column align-items-center align-items-sm-start px-3 pt-2 text-white min-vh-100">
          <a href="/" class="d-flex align-items-center pb-3 mb-md-0 me-md-auto text-white text-decoration-none">
            <span class="fs-5 d-none d-sm-inline">Меню</span>
          </a>
          <ul class="nav nav-pills flex-column mb-sm-auto mb-0 align-items-center align-items-sm-start" id="menu">
            <li class="nav-item">
              <router-link to="/" class="nav-link align-middle px-0">
                <i class="fs-4 bi-house"></i> <span class="ms-1 d-none d-sm-inline">Выход</span>
              </router-link>
            </li>
            <li>
              <router-link to="/StatisticComponent" class="nav-link px-0 align-middle">
                <i class="fs-4 bi-speedometer2"></i> <span class="ms-1 d-none d-sm-inline">Статистика</span>
              </router-link>
            </li>
            <li>
              <router-link to="/AddFin" class="nav-link px-0 align-middle">
                <i class="fs-4 bi-table"></i> <span class="ms-1 d-none d-sm-inline">Добавить</span>
              </router-link>
            </li>
            <li>
              <router-link to="/allfin" class="nav-link px-0 align-middle">
                <i class="fs-4 bi-people"></i> <span class="ms-1 d-none d-sm-inline">Все</span>
              </router-link>
            </li>
          </ul>
          <hr>
          <div class="dropdown pb-4">
            <a href="#" class="d-flex align-items-center text-white text-decoration-none dropdown-toggle" id="dropdownUser1" data-bs-toggle="dropdown" aria-expanded="false">
              <img src="https://i.pinimg.com/736x/bb/6b/ba/bb6bbadfe2b4c6c956cd580eca997343.jpg" alt="hugenerd" width="30" height="30" class="rounded-circle">
              <span class="d-none d-sm-inline mx-1">{{ userName }}</span> <!-- Отображаем имя пользователя -->
            </a>           
          </div>
        </div>
      </div>
      <div class="col py-3">
        <router-view /> <!-- Здесь будут отображаться компоненты -->
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SidebarComponent',
  data() {
    return {
      userName: '', // Переменная для хранения имени пользователя
    };
  },
  created() {
    this.loadUserName(); // Загружаем имя пользователя при создании компонента
  },
  methods: {
    loadUserName() {
      const cookies = document.cookie.split('; '); // Получаем все cookies
      const userCookie = cookies.find(cookie => cookie.startsWith('userName=')); // Ищем cookie с именем пользователя
      if (userCookie) {
        this.userName = userCookie.split('=')[1]; // Извлекаем значение имени пользователя
      } else {
        this.userName = 'Гость'; // Значение по умолчанию, если cookie не найден
      }
    },
  },
};
</script>

<style scoped>
/* Добавьте свои стили, если необходимо */
</style>
<template>
    <div class="container-fluid">
      <div class="row flex-nowrap">
        <div class="col-auto col-md-3 col-xl-2 px-sm-2 px-0 bg-dark">
          <SidebarComponent /> <!-- Используем компонент Sidebar -->
        </div>
        <div class="col py-3">
          <div class="container mt-5">
            <h1 class="text-center">Добавить Транзакцию</h1>
            <form @submit.prevent="handleSubmit" id="transaction-form" class="shadow p-4 rounded bg-light text-center">
              <div class="form-group mb-3">
                <input
                  type="number"
                  class="form-control"
                  placeholder="Сумма"
                  v-model="amount"
                  required
                />
              </div>
              <div class="form-group mb-3">
                <select class="form-control" v-model="category" required>
                  <option value="">Выберите категорию</option>
                  <option v-for="cat in categories" :key="cat.id" :value="cat.name">{{ cat.name }}</option>
                </select>
              </div>
              <button type="submit" class="btn btn-primary btn-block mb-3">Добавить</button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import SidebarComponent from './SidebarComponent.vue'; // Импортируем компонент Sidebar
  
  export default {
    name: 'AddFin',
    components: {
      SidebarComponent, // Регистрируем компонент
    },
    data() {
      return {
        amount: null,
        category: '',
        categories: [], // Массив для хранения категорий
      };
    },
    created() {
      this.fetchCategories(); // Загружаем категории при создании компонента
    },
    methods: {
      fetchCategories() {
        fetch('http://localhost:8485/categories') // Замените на реальный URL вашего API
          .then(response => {
            if (!response.ok) {
              throw new Error('Network response was not ok');
            }
            return response.json();
          })
          .then(data => {
            this.categories = data; // Предполагается, что сервер возвращает массив категорий
          })
          .catch(error => {
            console.error('Ошибка при загрузке категорий:', error);
          });
      },
      handleSubmit() {
        const transactionData = {
          amount: this.amount,
          category: this.category
        };
        this.createTransaction(transactionData); // Вызываем метод для создания транзакции
      },
      createTransaction(transactionData) {
        fetch('http://localhost:8485/add_transaction', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(transactionData),
        })
        .then(response => {
          if (!response.ok) {
            throw new Error('Network response was not ok');
          }
          return response.json();
        })
        .then(data => {
          console.log('Транзакция успешно добавлена:', data);
          this.resetForm(); // Сбрасываем форму после успешного добавления
        })
        .catch(error => {
          console.error('Ошибка при добавлении транзакции:', error);
        });
      },
      resetForm() {
        this.amount = null;
        this.category = '';
      },
    },
  };
  </script>

  <style scoped>
.container {
  max-width: 700px; /* Ограничиваем ширину контейнера */
}

h1 {
  font-size: 2rem; /* Увеличиваем размер заголовка */
  color: #333; /* Цвет заголовка */
}

form {
  background-color: #f8f9fa; /* Светлый фон для формы */
  border-radius: 8px; /* Закругленные углы */
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1); /* Тень для формы */
  padding: 20px;
}

.form-control {
  border-radius: 5px; /* Закругленные углы для полей ввода */
 
}

.btn {
  border-radius: 5px; /* Закругленные углы для кнопки */
}
  </style>
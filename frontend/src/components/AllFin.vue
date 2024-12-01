<template>
  <div class="container-fluid">
    <div class="row flex-nowrap">
      <div class="col-auto col-md-3 col-xl-2 px-sm-2 px-0 bg-dark">
        <SidebarComponent /> <!-- Используем компонент Sidebar -->
      </div>
      <div class="col py-3">
        <div class="container mt-5">
          <h1 class="text-center mb-4">Список Транзакций</h1>
          <div class="form-group mb-3">
            <div class="col">
              <input type="date" class="form-control" v-model="filterDate" />
            </div>
            <div class="col">
              <select class="form-control" v-model="filterCategory">
                <option value="">Все категории</option>
                <option v-for="category in categories" :key="category" :value="category">{{ category }}</option>
              </select>
            </div>
            <div class="col">
              <button class="btn btn-info" @click="filterTransactions">Фильтровать</button>
            </div>
          </div>

          <table class="table table-striped">
            <thead>
              <tr>
                <th>Дата</th>
                <th>Категория</th>
                <th>Сумма</th>
                <th>Действия</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="transaction in filteredTransactions" :key="transaction.id">
                <td>{{ transaction.date }}</td>
                <td>{{ transaction.category }}</td>
                <td>{{ transaction.amount }}</td>
                <td>
                  <button class="btn btn-danger" @click="deleteTransaction(transaction.id)">Удалить</button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import SidebarComponent from './SidebarComponent.vue'; // Импортируем компонент Sidebar

export default {
  name: 'AllFin',
  components: {
    SidebarComponent, // Регистрируем компонент
  },
  data() {
    return {
      filterDate: '',
      filterCategory: '',
      transactions: [], // Массив для хранения транзакций
      categories: [], // Массив для хранения категорий
    };
  },
  created() {
    this.fetchTransactions(); // Загружаем транзакции при создании компонента
    this.fetchCategories(); // Загружаем категории при создании компонента
  },
  computed: {
    filteredTransactions() {
      return this.transactions.filter(transaction => {
        const matchesDate = this.filterDate ? transaction.date === this.filterDate : true;
        const matchesCategory = this.filterCategory ? transaction.category === this.filterCategory : true;
        return matchesDate && matchesCategory;
      });
    },
  },
  methods: {
    fetchTransactions() {
      fetch('http://localhost:8485/all_transaction')
        .then(response => {
          if (!response.ok) {
            throw new Error('Network response was not ok');
          }
          return response.json();
        })
        .then(data => {
          this.transactions = data;
        })
        .catch(error => {
          console.error('Ошибка при загрузке транзакций:', error);
        });
    },
    fetchCategories() {
      fetch('http:/localhost:8485/categories') // Замените на реальный URL вашего API
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
    filterTransactions() {
      // Логика фильтрации уже реализована в computed свойстве filteredTransactions
      console.log('Фильтры применены:', {
        date: this.filterDate,
        category: this.filterCategory,
      });
    },
    deleteTransaction(id) {
      // Отправляем запрос на удаление транзакции на сервер
      fetch(`http://localhost:8485/transactions/${id}`, { // Замените на реальный URL вашего API
        method: 'DELETE',
      })
        .then(response => {
          if (!response.ok) {
            throw new Error('Ошибка при удалении транзакции');
          }
          // Удаляем транзакцию из локального массива, если удаление на сервере прошло успешно
          this.transactions = this.transactions.filter(transaction => transaction.id !== id);
          console.log(`Транзакция с ID ${id} удалена`);
        })
        .catch(error => {
          console.error('Ошибка при удалении транзакции:', error);
        });
    }
  },
};
</script>


<style scoped>
.container {
  max-width: 800px;
  /* Ограничиваем ширину контейнера */
}

h1 {
  font-size: 2rem;
  /* Увеличиваем размер заголовка */
  color: #333;
  /* Цвет заголовка */
}

.table {
  margin-top: 20px;
  /* Добавляем отступ сверху для таблицы */
}

.btn-info {
  margin-top: 0;
  /* Убираем верхний отступ для кнопки фильтрации */
}
</style>
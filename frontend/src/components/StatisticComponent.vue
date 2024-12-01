<template>
  <div class="row flex-nowrap">
    <div class="col-auto col-md-3 col-xl-2 px-sm-2 px-0 bg-dark">
      <SidebarComponent /> <!-- Используем компонент Sidebar -->
    </div>
    <div class="col py-3">
      <div class="container mt-5">
        <h1 class="text-center mb-4">Статистика</h1>
        <div class="form-group mb-3">
          <div class="col">
            <input type="date" class="form-control" v-model="startDate" required />
          </div>
          <div class="col">
            <input type="date" class="form-control" v-model="endDate" required />
          </div>
          <div class="col">
            <button class="btn btn-primary btn-block mb-3" @click="generateReport">Сгенерировать отчет</button>
          </div>
        </div>

        <div id="report" v-if="reportGenerated" class="mt-4">
          <h2>Общая сумма доходов: <span id="total-income">{{ totalIncome }}</span></h2>
          <h2>Общая сумма расходов: <span id="total-expense">{{ totalExpense }}</span></h2>
          <canvas id="expense-chart" ref="expenseChart" class="mt-4"></canvas>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import SidebarComponent from './SidebarComponent.vue'; // Импортируем компонент Sidebar
import { Chart } from 'chart.js'; // Импортируем Chart.js для построения графиков

export default {
  name: 'StatisticComponent',
  components: {
    SidebarComponent, // Регистрируем компонент
  },
  data() {
    return {
      startDate: '',
      endDate: '',
      totalIncome: 0,
      totalExpense: 0,
      reportGenerated: false,
      expenseChart: null,
    };
  },
  methods: {
    generateReport() {
      // Здесь вы можете добавить логику для расчета доходов и расходов
      // Для примера, мы просто зададим фиксированные значения
      this.totalIncome = 1000; // Замените на реальную логику
      this.totalExpense = 500; // Замените на реальную логику
      this.reportGenerated = true;

      // Генерация графика
      this.createChart();
    },
    createChart() {
      const ctx = this.$refs.expenseChart.getContext('2d');
      if (this.expenseChart) {
        this.expenseChart.destroy(); // Удаляем предыдущий график, если он существует
      }
      this.expenseChart = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: ['Доходы', 'Расходы'],
          datasets: [{
            label: 'Сумма',
            data: [this.totalIncome, this.totalExpense],
            backgroundColor: ['#4CAF50', '#F44336'],
            borderColor: ['#388E3C', '#D32F2F'],
            borderWidth: 1,
          }],
        },
        options: {
          scales: {
            y: {
              beginAtZero: true,
            },
          },
        },
      });
    },
  },
};
</script>

<style scoped>
.container {
  max-width: 800px; /* Ограничиваем ширину контейнера */
  margin: auto; /* Центрируем контейнер */
  padding: 20px; /* Добавляем отступы */
  background-color: #ffffff; /* Белый фон для контейнера */
  border-radius: 10px; /* Закругленные углы */
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1); /* Тень для контейнера */
}

h1 {
  font-size: 2rem; /* Увеличиваем размер заголовка */
  color: #333; /* Цвет заголовка */
  margin-bottom: 20px; /* Отступ снизу */
}

h2 {
  color: #555; /* Цвет подзаголовков */
  margin: 10px 0; /* Отступы сверху и снизу */
}

#report {
  background-color: #f8f9fa; /* Светлый фон для отчета */
  border-radius: 8px; /* Закругленные углы */
  padding: 20px; /* Отступы внутри блока отчета */
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1); /* Тень для блока отчета */
  margin-top: 20px; /* Отступ сверху */
}

.form-group {
  display: flex; /* Используем flexbox для выравнивания элементов */
  justify-content: space-between; /* Распределяем элементы по ширине */
  margin-bottom: 20px; /* Отступ снизу */
}

input[type="date"] {
  border: 1px solid #ced4da; /* Цвет границы */
  border-radius: 5px; /* Закругленные углы */
  padding: 10px; /* Отступы внутри поля */
  transition: border-color 0.3s; /* Плавный переход цвета границы */
}

input[type="date"]:focus {
  border-color: #007bff; /* Цвет границы при фокусе */
  outline: none; /* Убираем стандартный контур */
}

button {
  background-color: #007bff; /* Цвет фона кнопки */
  color: white; /* Цвет текста кнопки */
  border: none; /* Убираем границу */
  border-radius: 5px; /* Закругленные углы */
  padding: 10px 20px; /* Отступы внутри кнопки */
  cursor: pointer; /* Указатель при наведении */
  transition: background-color 0.3s; /* Плавный переход цвета фона */
}

button:hover {
  background-color: #0056b3; /* Цвет фона при наведении */
}

canvas {
  max-width: 100%; /* Ограничиваем ширину графика */
  height: auto; /* Автоматическая высота для графика */
  margin-top: 20px; /* Отступ сверху */
}
</style>
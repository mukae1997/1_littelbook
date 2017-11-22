
import Book from './components/Book'
import BookList from './components/booklist.vue'
export default [  // 注意export的是一个数组，其实可以写在上面的routes字段里
  // 在这里做路由，决定要显示的component，其实并没有刷新服务器
 {path:"/", component: BookList},
 {path:"/read", component: Book}
];

<template>
  <el-container>
    <el-aside width="200px">
      <el-menu>
        <el-menu-item index="-1">
          <i class="el-icon-s-fold" @click="getAllFoods">浏览所有</i>
        </el-menu-item>
        <el-menu-item
          v-for="(item,i) in AllFoodsCategory"
          :key="item.pk"
          :index="i.toString()"
          @click="getFoodsByCategory(item.pk)"
        >{{item.fields.name}}</el-menu-item>
      </el-menu>
    </el-aside>
    <el-main>
      <router-link :to="'/foodinfo/'+good.id" tag="div" v-for="(good) in foodsList" :key="good.id">
        <el-card :body-style="{ padding: '1px' }">
          <div class="image-container">
            <img :src="good.picUrl1" class="image" alt="呀 图片丢失了" />
          </div>
          <div>
            <div class="name-price">
              <span class="s-name">{{good.name}}</span>
              <div v-if="ism">
                <el-button
                  type="danger"
                  style="width:100px;height:20px;line-height:1px;"
                  @click="deleteFood(good.id)"
                >删除</el-button>
              </div>
              <span class="s-price">¥{{good.amount_money}}</span>
            </div>
            <div class="category-more">
              <span class="s-category">{{good.category_id}}</span>
              <el-button type="text" class="button">了解更多</el-button>
            </div>
          </div>
        </el-card>
      </router-link>
      <el-row>
        <el-col :span="16" :offset="7">
          <el-pagination
          v-if="nowCategoryId==0"
            @current-change="pageChange"
            @prev-change="pageChange"
            @next-change="pageChange"
            :page-count="pageNum"
            layout="prev, pager, next"
          ></el-pagination>
        </el-col>
      </el-row>
    </el-main>
  </el-container>
</template>

<script>
export default {
  created() {
    this.getAllFoodsCategory();
    this.getAllFoods();
    this.getPageNum();
  },
  data() {
    return {
      foodsList: [],
      AllFoodsCategory: [],
      page: 1,
      nowCategoryId: 0,
      pageNum: 0
    };
  },
  computed: {
    // isManager: this.$store.getters.isManager

    ism() {
      return this.$store.state.isManager;
    }
  },
  methods: {
    getPageNum() {
      this.$http.get("api/get_all_page").then(result => {
        if (result.body.error_num == 0) {
          this.pageNum = result.body.allPage;
        } else {
          this.$message({
            duration: 1000,
            type: "error",
            message: "获取页数不成功，请重试"
          });
        }
      });
    },
    getAllFoodsCategory() {
      this.$http.get("api/get_all_food_category").then(result => {
        if (result.body.error_num == 0) {
          this.AllFoodsCategory = result.body.list;
        } else {
          this.$message({
            duration: 1000,
            type: "error",
            message: "获取分类列表不成功，请重试"
          });
        }
      });
    },
    getAllFoods() {
      this.nowCategoryId = 0;
      this.$http.get("api/get_page_food?page=" + this.page).then(result => {
        this.foodsList = [];
        result.body.list.forEach(element => {
          var obj = element.fields;
          obj.id = element.pk;
          this.foodsList.push(obj);
        });
      });
    },
    getFoodsByCategory(id) {
      this.nowCategoryId = id;
      this.page = 1;
      this.$http
        .get(
          "api/get_page_food_by_category?page=" +
            this.page +
            "&category_id=" +
            id
        )
        .then(result => {
          this.foodsList = [];
          result.body.list.forEach(element => {
            var obj = element.fields;
            obj.id = element.pk;
            this.foodsList.push(obj);
          });
        });
    },
    deleteFood(id) {
      this.$http.get("api/delete_food?foodid=" + id).then(result => {
        if (result.body.error_num == 0) {
          this.$message({
            duration: 1000,
            type: "info",
            message: "删除成功"
          });
        } else {
          this.$message({
            duration: 1000,
            type: "error",
            message: "删除失败"
          });
        }
      });
      this.$route.go(0);
    },
    pageChange(val) {
      console.log(val);
      this.page=val
      this.getAllFoods()
    }
  }
};
</script>

<style lang="scss" scoped>
.el-container {
  margin-top: 25px;
  margin-right: 10%;
  margin-left: 10%;
}
.el-aside {
  color: #333;
  background-color: #ffffff;
  // .el-menu {
  //   border: 0.1px solid #ccc;
  //   box-shadow: 0 0 8px #ccc;
  //   border-radius: 4%;
  // }
}
.time {
  font-size: 15px;
  color: #999;
}

.bottom {
  margin-top: 13px;
  line-height: 12px;
}

.button {
  padding: 0;
  float: right;
}

.image {
  width: 100%;
  display: block;
}
.el-main {
  flex-wrap: wrap;
  padding: 7px;
  justify-content: space-between;
  display: flex;

  .el-card {
    // border: 0.1px solid #ccc;
    box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
    border-radius: 4%;
    margin: 5px;
    width: 220px;
    height: 290px;
    flex-direction: column;
    justify-content: space-between;
    .image-container {
      width: 218px;
      height: 221px;
      img {
        width: auto;
        text-align: center;
        height: 221px;
        overflow: hidden;
      }
    }

    .name-price {
      display: flex;
      justify-content: space-between;
      .s-name {
        font-size: 18px;
      }

      .s-price {
        padding-top: 24px;
        color: red;
        font-weight: bold;
        font-size: 20px;
      }
    }
    .category-more {
      margin: 0;
      display: flex;
      justify-content: space-between;
      .s-category {
        font-size: 12px;
      }
    }
  }
}

// .clearfix:before,
// .clearfix:after {
//   display: table;
//   content: "";
// }

// .clearfix:after {
//   clear: both;
// }
</style>
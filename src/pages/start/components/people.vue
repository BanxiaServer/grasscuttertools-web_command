
<script setup lang="ts">
import { reactive, ref, computed } from 'vue'
import { useClipboard } from '@vueuse/core'
import { Message } from '@arco-design/web-vue'
import { useAppStore } from '@/store/modules/app'

import people from './json/people.json'
const { text, isSupported, copy } = useClipboard()
const appStore = useAppStore()

var value2 = ref(1002)//输入框默认数值
var grade = ref(90)//等级
var num = ref(6)//命座
var chua_grade = ref(10)//天赋等级

const value = computed(() => {
  return `/give ${value2.value} lv${grade.value} c${num.value} sl${chua_grade.value}`
})
const options = reactive(people)
const message = Message

function copyvalue() {
  copy(value.value)
  if (isSupported) {
    message.success(`已复制${value.value}`)
  }
}
const send: any = inject("send")
</script>

<template>
  <div class="commuse">
    <div class="commuse-item">
      <div class="text-slate-900 dark:text-slate-100"> 怪物: </div>
      <a-cascader allow-search v-model="value2" :options="options" placeholder="" filterable />
    </div>
    <div class="commuse-item">
      <div class="text-slate-900 dark:text-slate-100"> 等级: </div>
      <a-input-number v-model="grade" placeholder="请输入数量" mode="button" size="large" class="input-demo" />
    </div>
    <div class="commuse-item">
      <div class="text-slate-900 dark:text-slate-100"> 命座: </div>
      <a-input-number v-model="num" placeholder="请输入数量" mode="button" size="large" class="input-demo" />
    </div>
    <div class="commuse-item">
      <div class="text-slate-900 dark:text-slate-100"> 天赋等级: </div>
      <a-input-number v-model="num" placeholder="请输入数量" mode="button" size="large" class="input-demo" />
    </div>
    <div class="generate">
      <a-input v-model="value" placeholder="" />
      <a-button type="outline" @click="copyvalue">复制</a-button>
      <a-button type="outline" v-if="appStore.isLogin" @click="send(value)">执行</a-button>
    </div>
  </div>
</template>
<style lang="less" scoped>
.commuse {
  width: 500px;
  margin: auto;
}

.commuse-item {
  display: flex;
  align-items: center;
  color: #000;
  margin: 18px 0;

  >div {
    &:nth-child(1) {
      width: 150px;
      text-align: right;
      padding-right: 10px;
    }
  }
}

.generate {
  display: flex;
  align-items: center;
  margin-left: 100px;
}
</style>

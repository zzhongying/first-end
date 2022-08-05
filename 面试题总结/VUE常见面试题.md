## 零、基础补充

### 1.发布-订阅模式

**定义：**订阅发布模式定义了一种一对多的依赖关系，让多个订阅者对象同时监听某一个主题对象。这个主题对象在自身状态变化时，会通知所有订阅者对象，使它们能够自动更新自己的状态

典型案例：在dom节点上绑定过事件函数，那么我们就曾经使用过发布-订阅模式。

```js
document.getElementById('test').addEventListener('click',function(){ alert(2)},fasle;)
```

我们订阅document.body上的click事件，当body被点击时，body便会向订阅者发布这个消息。

VUE中的事件总线就是使用的发布订阅模式

### 2.观察者模式

目标者对象和观察者对象有相互依赖的关系，观察者对某个对象的状态进行观察，如果对象的状态发生改变，就会通知所有依赖这个对象的观察者。

例：Vue中响应式数据变化是**观察者模式**。每个响应式属性都有**dep**，**dep**存放了依赖这个属性的**watcher**，**watcher**是观测数据变化的函数，如果数据发生变化，**dep**就会通知所有的观察者watcher去调用更新方法。每个watcher中也存放了dep，帮助watcher知道是哪个dep通知了自己

### 2.数据劫持

**定义：**给数据添加监听，一旦数据发生变化，就执行视图的修改操作，这个过程就是**数据劫持**。

**双向绑定：**双向绑定其实就是，UI或者数据有一方做了修改，那么另外一个也会随着改变。视图驱动数据，这个很简单，我们只要绑定事件就可以，但是数据要怎么驱动视图呢？这里就需要去对数据做监听，我们通常称之为”数据劫持“。在每一次数据改变的时候，去执行更新视图的操作。（v-model是典型的双向绑定）

### 3. MVC, MVP,MVVM

#### 3.1 MVC

- Model负责业务数据的存储以及相对于数据的操作。
- View负责页面的显示逻辑。
  - Controller是view和model的纽带，当用户与页面**产生交互**时，controller中的时间触发器调用model层，完成对model的修改。model和view是观察者模式，**当model发生变化时，通知并驱动view发生相应的改变**。View捕获用户交互操作后直接转发给Contoller，后者**完成相应的UI逻辑**。如果需要涉及业务功能的调用，Contoller会直接调用Model及修改Model状态。Contoller也可以主动控制原View或创建新的View对用户交互操作予以响应。这也表明MVC之间的通信是单向的

**缺点：**

- 因为model通知view发生改变，所以**View 层和 Model 层耦合**在一起，当项目逻辑变得复杂的时候，可能会造成代码的混乱，并且可能会对代码的复用性造成一些问题
- MVC中view层和controller层一般是一一对应的，这样view无法抽象复用，增加了冗余代码。

![image-20220709145125469](C:\Users\SFONE\AppData\Roaming\Typora\typora-user-images\image-20220709145125469.png)

#### 3.2 MVP

分为model，view和presenter。由于MVC中model和view存在耦合性问题，MVP使用presenter来解耦。MVP 模式中，View 层的接口暴露给了 Presenter， 因此可以在 Presenter 中将 Model 的变化和 View 的变化绑定在一起，以此来实现 View 和 Model 的同步更新。这样就实现了对 View 和 Model 的解耦，Presenter 还包含了其他的响应逻辑。**MVP中严格禁止View和Model间的直接交互**，必需通过Presenter来完成。Model的独立性得到了真正的体现，它不仅仅与可视化元素的呈现（View）无关，与UI处理逻辑也无关。使用MVP的应用是**用户驱动**而不是Model驱动，所以**Model不需要主动通知view**

**缺点：**

- View非常薄，不部署任何业务逻辑，没有任何主动性

- Presenter非常厚，所有的交互都发生在Presenter内部，需要**处理业务逻辑并且处理页面参数获取及显示更新**，只适合小型项目，大项目会导致Presenter非常臃肿。（为了处理Presenter臃肿问题，于是有了VM的数据双向绑定，处理了获取和更新页面数据的问题。）
- **视图和Presenter的交互会过于频繁，联系过于紧密，耦合度过高，view变更，presenter也要变更**



**MVC和MVP之间的区别**：

- 在**MVC**中，**View与Model层直接交互，读取数据，不通过Controller**

- 在**MVP**中，**View与Model层不直接交互，而是通过Presenter，所有的交互都是发生在Presenter 的内部**

  ![image-20220709145114346](C:\Users\SFONE\AppData\Roaming\Typora\typora-user-images\image-20220709145114346.png)



#### 3.3 MVVM

- Model： Model代表数据模型，数据和业务逻辑都在Model层中定义（JS中的ajax，axios）
- View：代表UI视图，负责数据的展示（html，css），结构，布局，外观，响应式
- ViewModel： 通过实现一套数据响应式机制自动响应Model中数据变化，同时 Viewmodel 会实现一套更新策略自动将数据变化转换为视图更新； 

MVVM模式与MVP模式的区别是，它采用双向绑定（data-binding）：View的变动，自动反应在ViewModel，反之亦然。View、Angular和Ember都采用这种模式。MVVM 设计模式**将view层的布局控件和model层的数据通过中间桥梁viewModel实现双向绑定**，而view和model没有直接的交互，实现了view和model的解耦。ViewModel和View之间的交互通过Data Binding实现双向交互，他能够监听到数据的变化，然后通知视图进行自动更新。

Model和ViewModel之间的交互是双向的，因此视图的数据的变化会同时修改数据源，而数据源数据的变化也会立即反应到View上，实现了 Model和View的数据自动同步，因此开发者只需要专注于数据的维护操作即可，而不需要自己操作DOM。Model和ViewModel之间的交互是双向的，因此视图的数据的变化会同时修改数据源，而数据源数据的变化也会立即反应到View上.

PS: 数据驱动视图的重点是**如何知道数据变了**，只要知道数据变了，那么接下去的事都好处理。如何知道数据变了，就是通过`Object.defineProperty( )`对属性设置一个set函数，当数据改变了就会来触发这个函数，所以我们只要将一些需要更新的方法放在这里面就可以实现data更新view了。

注：双向通信不等于双向绑定

![image-20220709145138660](C:\Users\SFONE\AppData\Roaming\Typora\typora-user-images\image-20220709145138660.png)

**优点：**

- 数据双向绑：减少基础代码，提高开发效率（由vm层提供，vm是MVVM的核心）
- 低耦合：视图（View）可以独立于Model变化和修改，一个ViewModel可以绑定到不同的"View"上，当View变化的时候Model可以不变，当Model变化的时候View也可以不变。
- 可重用性：你可以把一些视图逻辑放在一个ViewModel里面，让很多view重用这段视图逻辑。
- 独立开发：开发人员可以专注于业务逻辑和数据的开发（ViewModel），设计人员可以专注于页面设计，使用Expression Blend可以很容易设计界面并生成xml代码。
- 界面测试：界面素来是比较难于测试的，而现在测试可以针对ViewModel来写。

**缺点：**

- ⼀个⼤的模块中model也会很⼤，虽然使⽤⽅便了也很容易保证了数据的⼀致性，但是⻓期持有，不释放内存就造成了花费更多的内存 。双向绑定增加了大量的内存开销，增加了程序的编译时间，项目越大内存开销越大。
- 数据绑定使得 Bug 很难被调试。你看到界面异常了，有可能是你 View 的代码有 Bug，也可能是 Model 的代码有问题。数据绑定使得⼀个位置的Bug被快速传递到别的位置，要定位原始出问题的地⽅就变得不那么容易了。另外，数据绑定的声明是指令式地写在View的模版当中的，这些内容是没办法去打断点debug的 
- 对于⼤型的图形应⽤程序，视图状态较多，ViewModel的构建和维护的成本都会⽐较⾼

**总结：**

- 在MVC中，View会直接从Model中读取数据而不是通过 Controller；View和 Controller之间存在多对一关系。
- 在MVP中，View并不直接使用Model，它们之间的通信是通过Presenter (MVC中的Controller)来进行的，所有的交互都发生在Presenter内部；View和Presenter之间是一对一关系。
- MVVM 模式基本上与 MVP 模式完全一致，唯一的区别是：MVVM采用双向绑定（data-binding）：View的变动，自动反映在 ViewModel，反之亦然。

## 一、VUE概念方面

### 0.VUE的基本原理和优点

#### 1.0 前端框架为什么能流行？

前后分离的趋势：解放前端和后台的开发方式。

效率：降低开发成本和周期。

社区：各大框架都有一个很大的社区，便于解决遇到的问题。

标准：只要遵循框架的标准，让团队合作更容易。

体验：可以更好的开发出跟原生一样的应用。

工程化：可维护性和工程性有更大提升。

效率：前端框架封装好了很多的特性，可以直接使用，提升了代码开发的效率

可以将VUE的优点包装进去

#### 1.1 基本原理

当一个Vue实例创建时，Vue会遍历data中的属性，用 Object.defineProperty （vue3.0使用proxy ）将它们转为 getter/setter，并且在内部追踪相关依赖，在属性被访问和修改时通知变化。 每个组件实例都有相应的 watcher 程序实例，它会在组件渲染的过程中把属性记录为依赖，之后当依赖项的setter被调用时，会通知watcher重新计算，从而致使它们关联的组件得以更新。

核心思想是组件化和数据驱动

#### 1.2 对VUE设计原则的理解

- **渐进式JavaScript框架**：与其它大型框架不同的是，Vue被设计为可以**自底向上逐层应用**。Vue的核心库只关注视图层，不仅易于上手，还便于与第三方库或既有项目整合。另一方面，当与现代化的工具链以及各种支持类库结合使用时，Vue也完全能够为复杂的单页应用提供驱动。

  >渐进式：**没有多做职责之外的事**，只做了自己该做的事，没有做不该做的事，仅此而已。更直白一点就是，用你想用或者能用的功能特性，你不想用的部分功能可以先不用。VUE不强求一次性接受并使用它的全部功能特性。

- 易用性：vue提供数据响应式、声明式模板语法和基于配置的组件系统等核心特性。这些使我们只需要关注应用的核心业务即可，只要会写js、html和css就能轻松编写vue应用。

- 灵活性：渐进式框架的最大优点就是灵活性，如果应用足够小，我们可能仅需要vue核心特性即可完成功能；随着应用规模不断扩大，我们才可能逐渐引入路由、状态管理、vue-cli等库和工具，不管是应用体积还是学习难度都是一个逐渐增加的平和曲线。

- 高效性：超快的虚拟DOM和diﬀ算法使我们的应用拥有最佳的性能表现。追求高效的过程还在继续，vue3中引入Proxy对数据响应式改进以及编译器中对于静态内容编译的改进都会让vue更加高效。

#### 1.3 优点

- 轻量级框架：只关注视图层，是一个构建数据的视图集合，大小只有几十kb；
- 简单易学：国人开发，中文文档，不存在语言障碍 ，易于理解和学习；
- 双向数据绑定：保留了angular的特点，在数据操作方面更为简单；
- 组件化：保留了react的优点，实现了html的封装和重用，在构建单页面应用方面有着独特的优势；
- 视图，数据，结构分离：使数据的更改更为简单，不需要进行逻辑代码的修改，只需要操作数据就能完成相关操作；
- 虚拟DOM：dom操作是非常耗费性能的， 不再使用原生的dom操作节点，极大解放dom操作，但具体操作的还是dom不过是换了另一种方式；
- 运行速度更快:相比较与react而言，同样是操作虚拟dom，就性能而言，vue存在很大的优势。

#### 1.4 常见的VUE性能优化方法

**1.路由懒加载**：如果没有用懒加载，就会导致进入首页时需要加载的内容过多，时间过长，就会出现长时间的白屏，很不利于用户体验，SEO 也不友好

```js
const router = new VueRouter({routes:[
    {
        path:'/foo',
        component:()=> import ('./Foo.vue')  //ES6写法
        component:require('@/components/Foo.vue').default
    }
]})
```

**2.图片懒加载：**对于图片过多的页面，为了加速页面加载速度，所以很多时候我们需要将页面内未出现在可视区域内的图片先不做加载， 等到滚动到可视区域后再去加载。

```html
<img v-lazy='./static/img/1.png'>
```

**3.使用keep-alive缓存页面：**通过内置组件 `<keep-alive></keep-alive>` 来把组件缓存起来，在组件切换的时候不进行卸载，这样当再次返回的时候，就能从缓存中快速渲染，而不是重新渲染，以节省性能

```html
<tamplate>
    <div>
        <keep-alive> <child></child> </keep-alive>
    </div>
</tamplate>
```

**4.不同时使用v-if和v-for**：如果必须使用，则将v-if放在v-for的外围

```html
<template>
    <ul v-if = 'isAcitve'>
        <li v-for='user in activeUser'> {{ user.name }} </li>
    </ul>
</template>
```

**5.第三方组件按需插入**：像element-ui或者bootstrap按需引入

```js
import { Button, Select } from 'element-ui';
```

**6.使用v-show复用组件，而不是v-if。**当DOM结构越复杂，使用v-show的受益就越大。不过它也有劣势，就是 v-show 在一开始的时候，所有分支内部的组件都会渲染，对应的生命周期钩子函数都会执行，而 v-if 只会加载判断条件命中的组件，所以需要根据不同场景使用合适的指令

```html
<template>
  <div class="cell">
     <!--这种情况用v-show复用DOM，比v-if效果好-->
     <div v-show="value" class="on">
        <Heavy :n="10000"/>
     </div>
     <section v-show="!value" class="off">
        <Heavy :n="10000"/>
     </section>
  </div>
</template>
```

**7.将无状态的组件设置为函数组件：**对应一些纯展示，没有响应数据，没有状态管理，也不用生命周期钩子函数的组件，我们可以设置为函数式组件，提高渲染性能，因为会把它当成一个函数来处理，所以开销很低。

**原理**：在 `patch` 过程中对于函数式组件的 `render` 生成的虚拟 DOM，不会有递归子组件初始化的过程，所以渲染开销会低很多

它可以接受 `props`，但是由于不会创建实例，所以内部不能使用 `this.xx` 获取组件属性

```html
<template functional>
	<div class="cell">
		<div v-if="props.value" class="on"></div>
		<section v-else class="off"></section>
	</div>
</template>


<script>
	export default { props: ['value'] }
</script>
```

**8.长列表性能优化：**

- 如果列表是纯粹的数据展示，不会有任何改变，就不需要做响应话，比如使用 `Object.freeze()` 冻结一个对象，[MDN的描述是](https://link.segmentfault.com/?enc=4yGqHaTlBDigUjEDX97Agw%3D%3D.YUJvi6K%2FhSE4wvpvuupM8bSRTSX3P1ASR3V%2BnUceo%2FdPeIrnri2%2BkrCFxXqPj03dPkOE0pUBXlVMT%2BH24SW%2F%2BITo022qTYd6qomuTs3mBgzK9DJYn5ldqGUm5Aw2kpUD) 该方法冻结的对象不能被修改；即不能向这个对象添加新属性，不能删除已有属性，不能修改该对象已有属性的可枚举性、可配置性、可写性，以及不能修改已有属性的值，以及该对象的原型也不能被修改

- 如果是⼤数据⻓列表，可采⽤虚拟滚动，只渲染少部分(可视区域)区域的内容。原理是监听滚动事件，动态更新需要显示的 DOM，并计算出在视图中的位移，这也意味着在滚动过程需要实时计算，有一定成本，所以如果数据量不是很大的情况下，用普通的滚动就行

```JS
<recycle-scroller
  class="items"
  :items="items"
  :item-size="24"
>
  <template v-slot="{ item }">
    <FetchItemView
      :item="item"
      @vote="voteItem(item)"
    />
  </template>
</recycle-scroller>
```

**9.列表使用唯一key：**这样以后是添加一个值，而不是全部重新渲染

**10.变量本地化：**把多次引用的变量保存起来，因为每次访问 `this.xx` 的时候，由于是响应式对象，所以每次都会触发 `getter`，然后执行依赖收集的相关代码，如果使用变量次数越多，性能自然就越差

```js

<template> 
 <div :style="{ opacity: number / 100 }"> {{ result
}}</div>
</template>
<script>
import { someThing } from '@/utils'
export default {
 props: ['number'], 
 computed: {  
  base () { return 100 },  
  result () {   
   let base = this.base, number = this.number 
   // 保存起来    
  for (let i = 0; i < 1000; i++) {   
   number += someThing(base) // 避免频繁引用
this.xx   
  }   
   return number 
  }
}
}
</script>
```

**11.** 尽量减少data中的数据，data中的数据都会增加getter和setter，会收集对应的watcher

### 1. Vue是如何收集依赖的？

在初始化 Vue 的每个组件时，会对组件的 data 进行初始化，就会将由普通对象变成响应式对象，在这个过程中便会进行依赖收集的相关逻辑，

#### 1.理解Dep

​	Dep是一个订阅者，主要用于存放watcher观察者对象，每一个Data属性都会创建一个Dep，用来搜集所有使用到这个Data的Watcher对象。所以一个项目中会有多个观察者。但是由于JS是单线程的，所以在同一时刻，只有一个观察者在执行，可以使用Dep.target判断当前观察者是哪一个Dep。

#### 2.理解watcher

由于 Vue 执行一个组件的 `render` 函数是由 `Watcher` 去代理执行的，`Watcher` 在执行前会把 `Watcher` 自身先赋值给 `Dep.target` 这个全局变量，等待响应式属性去收集它。这样在哪个组件执行 `render` 函数时访问了响应式属性，响应式属性就会精确的收集到当前全局存在的 `Dep.target` 作为自身的依赖。在响应式属性发生更新时通知`watcher`去重新调用vm.update( vm.render() )进行组件的视图更新。watcher分为三种，但是任何类型的`Watcher`都是基于`数据响应式`的，也就是说，要想实现`Watcher`，就需要先实现`数据响应式`，而`数据响应式`的原理就是通过`Object.defineProperty`去劫持变量的`get`和`set`属性：

- `渲染Watcher`：变量修改时，负责通知HTML里的**重新渲染 **

- `computed Watcher`：变量修改时，负责通知computed里依赖此变量的computed**属性变量**的修改

- `user Watcher`：变量修改时，负责通知watch属性里所对应的**变量函数**的执行。

### 2.Vue的响应数据绑定原理

VUE 采用MVVM模式实现双向绑定，所以涉及到MVVM中View和Model的双向绑定操作，而数据驱动视图需要使用到“数据劫持”。在VUE2.X中，数据劫持通过`Object.defineProperty`来实现，VUE3.X中使用Proxy实现对象的监听。两者都是通过数据劫持和发布-订阅者模式的方式实现双向绑定。

![image-20220708105947866](C:\Users\SFONE\AppData\Roaming\Typora\typora-user-images\image-20220708105947866.png)

#### 2.1 Vue2.X

![VUE中的双向绑定](F:\面试相关\面试题总结\图片\VUE中的双向绑定.png

几个重要模块：

- `Observer`: 发布者，递归地监听对象上的所有属性，在属性值改变的时候，触发相应的`Watcher`。将数据进行劫持，使用`Object.defineProperty`对属性进行重定义
- `Dep`: 订阅者列表，链接`Observer`和`Watcher`的桥梁，每一个`Observer`对应一个`Dep`。是一个记录以来关系的，有一个内部数组subs，记录所有依赖的watcher。
- `Watcher`: 订阅者，当监听的数据值修改时，执行响应的回调函数，在`Vue`里面的更新模板内容。
- `Observer`中进行响应式的绑定，在数据被读的时候，触发`get`方法，执行`Dep`来收集依赖，也就是收集`Watcher`。在数据被改的时候，触发`set`方法，通过对应的所有依赖(`Watcher`)，去执行更新。比如`watch`和`computed`就执行开发者自定义的回调方法。
- `Object.defineProperty(obj,prop,descriptor)`会在一个对象上定义一个新属性，或者修改一个对象的现有属性，并返回此对象。`obj`表示要定义属性的对象，`prop`表示要定义或修改的属性名称或者symbol，`descriptor`表示要定义或修改的属性描述符。面试官又问了Object.defineProperty除了 set get外还有什么属性，我回答了configurable（布尔）、enumerable（布尔）、value（any）、writable（布尔）。

>要实现mvvm的双向绑定，就必须要实现以下几点： 1、实现一个数据监听器Observer，能够对数据对象的所有属性进行监听，如有变动可拿到最新值并通知订阅者 2、实现一个指令解析器Compile，对每个元素节点的指令进行扫描和解析，根据指令模板替换数据，以及绑定相应的更新函数 3、实现一个Watcher，作为连接Observer和Compile的桥梁，能够订阅并收到每个属性变动的通知，执行指令绑定的相应回调函数，从而更新视图 4、mvvm入口函数，整合以上三者

关键内容：

**原理**：Vue.js 是采用**数据劫持结合发布者-订阅者模式**的方式实现双向绑定。主要分为以下几个步骤：

1. 需要observe的数据对象进行递归遍历，包括子属性对象的属性，使用`Object.defineProperty()`重写了其中set和get方法。当给这个对象的某个值赋值，就会触发setter，那么就能监听到了数据变化

2. `compile`解析模板指令，将模板中的变量（`v-model`、`v-html`）替换成数据，然后初始化渲染页面视图，并将每个指令对应的节点绑定更新函数，添加监听数据的订阅者，一旦数据有变动，收到通知，更新视图

3. 由于 Vue 执行一个组件的 `render` 函数是由 `Watcher` 去代理执行的，`Watcher` 在执行前会把 `Watcher` 自身先赋值给 `Dep.target` 这个全局变量，等待响应式属性去收集它。这样在哪个组件执行 `render` 函数时访问了响应式属性，响应式属性就会精确的收集到当前全局存在的 `Dep.target` 作为自身的依赖。在响应式属性发生更新时通知`watcher`去重新调用`vm.update`( `vm.render() `)进行组件的视图更新。

   Watcher订阅者是Observer和Compile之间通信的桥梁，主要做的事情是: 

   - 给每个组件实例都有watcher对象，在组件自身实例化时往属性订阅器(dep)里面添加自己 (订阅者)，当watcher中依赖项的setter（dep）发生变化时，使用dep.notice通知watcher
- watcher收到变化后，调用自身的update()方法，重新计算，并触发Compile中绑定的回调，从而使关联的组件更新。
  
5. 当watcher中依赖项的setter被调用时，会通知watcher重新计算，从而使关联的组件更新

6. MVVM作为数据绑定的入口，整合Observer、Compile和Watcher三者，**通过Observer来监听自己的model数据变化，通过Compile来解析编译模板指令，最终利用Watcher搭起Observer和Compile之间的通信桥梁**，达到数据变化 -> 视图更新；视图交互变化(input) -> 数据model变更的双向绑定效果

>总结：初始化 data 时，通过`Object.defineProperty`设置属性的 getter 和 setter，使属性变为响应式，然后在执行某些操作（渲染操作，计算属性，自定义 watcher 等）时，创建一个 watcher，这个 watcher 在执行求值操作之前会将一个全局变量`Dep.target`指向自身，然后在求值操作过程中如果访问了响应式属性，就会把当前的`Dep.target`也就是 watcher 添加到属性的 dep 中，然后在下次更新响应式属性时，就会从 dep 中找出收集的 watcher，然后执行`watcher.update`，执行更新操作。
>
>watch方法对每个元素进行监听，发布订阅者模式订阅watch对象，发布watch对象中update方法

```js
const data = {
    name: '你不知道滴前端',
    age: 25,
    info: {
        address: '北京'
    },
    numbers: [1, 2, 3, 4]
};

function observerObject(target, name, value) {   //参数分别表示：目标对象，目标对象中的属性，传入数据的类型
    if (typeof value === 'object' || Array.isArray(target)) {   //如果传入的target是一个对象的话，则递归使用observer
        observer(value);
    }
    Object.defineProperty(target, name, {         //如果传入的值不是对象，则执行对目标属性的描述符（实现双向绑定）
        get() {
            return value;
        },
        set(newVal) {
            if (newVal !== value) {
                if (typeof value === 'object' || Array.isArray(value)) {        //继续递归
                    observer(value);
                }
                value = newVal;
            }
            renderView();                  //当目标类型为非对象时，准备修改属性内容时，执行renderView（执行视图渲染相关逻辑）                              
        }
    });
}

function observer(target) {                     
    if (typeof target !== 'object' || !target) {   //传入的如果不是对象而是属性，则将其加入到监听中
        return target;
    }
    for (const key in target) {                   //传入的是一个对象则递归调用 observe 遍历对象的每一个属性，确保 data 中的所有属性都加入监听。
        if (target.hasOwnProperty(key)) {
            const value = target[key];
            observerObject(target, key, value);
        }
    }
}
observer(data);
```

**`Object.defineProperty`的缺点：**

1. 无法检测到对象属性的新增或删除  

   由于js的动态性，可以为对象追加新的属性或者删除其中某个属性， 这点对经过Object.defineProperty方法建立的响应式对象来说，**只能追踪对象已有数据是否被修改**，无法追踪新增属性和删除属性， 这就需要另外处理，例如使用`vue.$set`。

2. 不能监听数组的变化（对数组基于下标的修改、对于 .length 修改的监测）   

   vue在实现数组的响应式时，缓存了array的原型链，重写了原型,它使用了一些hack, 把无法监听数组的情况通过重写数组的部分方法来实现响应式，这也只限制在数组的push/pop/shift/unshift/splice/sort/reverse七个方法，其他数组方法及数组的使用则无法检测到

```js
const oldArrayProperty = Array.prototype;
const newArrayProperty = Object.create(oldArrayProperty);    //是一种新的prototype
['pop', 'push', 'shift', 'unshift', 'splice'].forEach((method) => {
    newArrayProperty[method] = function() {
        renderView();          //执行视图渲染相关逻辑
        oldArrayProperty[method].call(this, ...arguments);   
        //call将oldArrayProperty[method]的this指向设置为 newArrayProperty[method]的this指向，就是给数组的每个方法添加一些视图渲染的操作
    };
});
 // 在observer函数中加入数组的判断，如果传入的是数组，则改变数组的原型对象为我们修改过后的原型。
    if (Array.isArray(target)) {
        target.__proto__ = newArrayProperty;
   }

//使用$set方法修改数组/对象
this.$set(this.arr, 0, "OBKoro1"); // 改变数组
this.$set(this.obj, "c", "OBKoro1"); // 改变对象
```

**object.definedProtery的缺陷：**

- 递归遍历所有的对象属性，当数据层级比较深的话，很耗费性能
- 虽然也能应用在数组上，但是需要修改数据的原型方法
- 只能够监听定义时的属性，不能监听新加的属性，这也就是为什么在vue中要使用Vue.set的原因，删除也是同理

Vue.$set的实现原理：

- 如果目标是数组，直接使用数组的 splice 方法触发响应式；
- 如果目标是对象，会先判读属性是否存在、对象是否是响应式，最终如果要对属性进行响应式处理，则是通过调用 defineReactive 方法进行响应式处理（ **defineReactive** 函数主要是利用 “Object.defineProperty” 函数作用于对象属性的值，进行取值和赋值操作时的拦截和处理)。
  - **读取** 属性时，触发 **getter**，将与响应式属性相关的vue实例保存起来。
  -  **修改** 属性时，触发 **setter**，更新与响应式属性相关的vue实例。

**Ovserve的监听过程:**

```js
    var Observe = function Observe(value) {
        
     if(typeof value !== 'object' || 'function'){
            //基础对象直接监听。。。
        Object.defineProperty(target, name, {         //如果传入的值不是对象，则执行对目标属性的描述符（实现双向绑定）
        get() {
            return value;
        },
        set(newVal) {
            if (newVal !== value) {
                if (typeof value === 'object' || Array.isArray(value)) {        //继续递归
                   Observer(value);
                }
                value = newVal;
            }
            renderView();                  //当目标类型为非对象时，准备修改属性内容时，执行renderView（执行视图渲染相关逻辑）                              
        }
    });
     }

    if(Array.isArray(value)){  //如果监听目标是数组，则调用数组监听方法
            this.observeArray(value)
        }else {   //如果监听的是对象，则调用对象监听方法
            this.observeObject(value)
        }

    }

    Observe.prototype.observeArray = function observeArray(items) {
        for(var i=0;i<items.length; i++){
            observe(items[i])
        }
    }

    // 遍历obj的属性，将obj对象的属性转化为响应式属性
    Observe.prototype.observeObject = function observeObject(items) {
        var key = Object.keys(items)
        for(var i=0;i<key.length;i++){   //递归遍历obj的所有属性
            // 给obj的每一个属性都赋予getter/setter方法。
            // 这样一旦属性被访问或者更新，这样我们就可以追踪到这些变化
            defineReactive(items, key[i], items[key[i]])
        }
    }xxxxxxxxxx        var Observe = function Observe(value) {        //基础对象直接监听。。。        if(Array.isArray(value)){  //如果监听目标是数组，则调用数组监听方法            this.observeArray(value)        }else {   //如果监听的是对象，则调用对象监听方法            this.observeObject(value)        }    }    Observe.prototype.observeArray = function observeArray(items) {        for(var i=0;i<items.length; i++){            observe(items[i])        }    }    // 遍历obj的属性，将obj对象的属性转化为响应式属性    Observe.prototype.observeObject = function observeObject(items) {        var key = Object.keys(items)        for(var i=0;i<key.length;i++){   //递归遍历obj的所有属性            // 给obj的每一个属性都赋予getter/setter方法。            // 这样一旦属性被访问或者更新，这样我们就可以追踪到这些变化            defineReactive(items, key[i], items[key[i]])        }    }var observe = function Ovserve()js
```

#### 2.2 Vue3.X

在vue3版本中，使用了proxy实现对象的监听，可以理解成，**在目标对象之前架设一层“拦截”**，外界对该对象的访问，都必须先通过这层拦截，因此提供了一种机制，可以对外界的访问进行过滤和改写。

**Refleact:**

Reflect是一个内建的对象，用来提供方法拦截JavaScript的操作。Reflect的所有属性和方法都是静态的(目前共有13个静态方法)，让Object操作都变成函数行为。

- Reflect不是一个函数对象，所以它是不可构造的，也就是说它不是一个构造器，不能通过new操作符去新建或者将其作为一个函数去调用Reflect对象。
- Reflect对象的方法与Proxy对象的方法一一对应，只要是Proxy对象的方法，就能在Reflect对象上找到对应的方法。
- 修改某些Object方法的返回结果，让其变得更规范化。如Object.defineProperty(obj, name, desc)在无法定义属性时，会抛出一个错误，而Reflect.defineProperty (obj, name, desc)则会返回false。

**优点：**

- proxy可以直接监听数组的修改
- proxy可以直接监听属性的新增和删除
- 在实现深度监听的时候，只有在data对象的属性被访问的时候，才去对这个属性做监听处理，而不是一次性递归所有的。

**缺点：**

存在兼容性问题，因为Proxy使用ES6

```js

function observe(target) {
    if (typeof target !== 'object' || target == null) {    //如果传入类型不是对象的话，则将该传入参数加入监听列表
        return target;
    }
    const obseved = new Proxy(target, {        //如果传入类型是对象的话
        get(target, key, receiver) {
            //只有在data对象的属性被访问时，才对这个属性做监听处理
           return observe(Reflect.get(target, key, receiver);)  //如果是get方法，则递归，直至target不是object类型
            //获取对象身上某个属性的值，类似于 target[name]。如果没有该属性，则返回undefined。
        },
        set(target, key, value, receiver) {
            if (value === target[key]) {
                return true;
            }
            const ownKeys = Reflect.ownKeys(target);   //返回一个包含所有自身属性（不包含继承属性）的数组。(类似于 Object.keys(), 但不会受enumerable影响, Object.keys返回所有可枚举属性的字符串数组).
            if (ownKeys.includes(key)) {
                console.log('旧属性');
            } else {
                console.log('新添加的属性');
           		return Reflect.set(target, key, value, receiver)
        	},
         deleteProperty(target, key) {
           return result  Reflect.deleteProperty(target, key);
        }
    });
    return obseved;
}


const data = {
    name: '你不知道的前端',
    age: 25,
    info: {
        city:'beijing'
    }，
    numbers: [1, 2, 3, 4]
};
const proxyData = observe(data)
```

### 2.VUE的两个核心点

答：数据驱动、组件系统

数据驱动：ViewModel，保证数据和视图的一致性。

组件系统：应用类UI可以看作全部是由组件树构成的。

### 3.VUE和jQuery的区别

1.jQuery是直接操作DOM，并且数据和界面是一起的，和原生JS相比只是更方便的操作了DOM。Vue不直接操作DOM，Vue的数据与视图是分开的，Vue只需要操作数据即可

2.在操作DOM频繁的场景里，jQuery的操作DOM行为是频繁的，而Vue利用虚拟DOM的技术，大大提高了更新DOM时的性能

3.Vue中不倡导直接操作DOM，开发者只需要把大部分精力放在数据层面上

4.Vue集成的一些库，大大提高开发效率，比如Vuex，Router等

### 4.对MVVM，MCV, MVP的理解

答：vue是实现了双向数据绑定的mvvm框架，当视图改变更新模型层，当模型层改变更新视图层。在vue中，使用了双向绑定技术，就是View的变化能实时让Model发生变化，而Model的变化也能实时更新到View。

### 5.你们VUE项目是打包了一个js文件，一个css文件，还是有多个文件？

答：根据vue-cli脚手架规范，在dist文件夹下存在css和js文件夹，里面分别有一个css文件和一个js文件

### 6.请说下封装 VUE 组件的过程和对VUE组件的理解(待补充-上传npm)

#### 1. VUE封装组件的过程

**1.新建Package文件夹：**

因为我们可能会封装多个组件，所以在src下面新建一个package文件夹用来存放所有需要上传的组件。

**2.编写组件代码，并引入APP.vue查看结果**

**3.使用VUE插件模式**

这一步是封装组件中的重点，用到了Vue提供的一个公开方法：install。这个方法会在你使用`Vue.use(plugin)`时被调用，这样使得我们的插件注册到了全局，在子组件的任何地方都可以使用。在package目录下新建index.js文件，代码如下：

```js
//package/index.js
import PigButton from "../package/pig-button/index.vue"; // 引入封装好的组件
const coms = [PigButton]; // 将来如果有其它组件,都可以写到这个数组里

// 批量组件注册
const install = function (Vue) {
  coms.forEach((com) => {
    Vue.component(com.name, com);  
      //将我们封装好的组件注册为全局组件，用到了Vue.component()方法，当使用Vue.use()时，我们的install方法便会执行。
      //Vue.use(plugin)
  });
};

export default install; // 这个方法以后再使用的时候可以被use调用
```

**4.组件打包:**  

修改我们项目得package.json文件，配置打包命令：

```js
 "scripts": {
    "serve": "vue-cli-service serve",
    "build": "vue-cli-service build",
    "lint": "vue-cli-service lint"
    "package": "vue-cli-service build --target lib ./src/package/index.js --name pig-ui --dest pig-ui"
  },

// package命令分别表示：
--target lib 关键字 指定打包的目录
--name 打包后的文件名字
--dest 打包后的文件夹的名称
```

**5.执行打包命令**

```js
npm run build
```

打包执行完成后我们项目目录下就会多出一个pig-ui文件夹，存放的是打包后的文件。

**6.发布到npm**

想要发布到npm仓库，我们还得在pig-ui文件夹下初始化一个package.json文件。进入pig-ui目录，执行命令：`npm init -y`,设置版本号，描述等

注册账号=》登录=》npm publish（注意包的名字不能重复）

```

//上传后会生成：
 "name": "expxgb",
  "version": "0.1.0",
  "private": false,
  "script":{
      ....
 }
```

#### 2.对VUE组件的理解

- 组件是独立和可复用的代码组织单元。组件系统是Vue核心特性之一，它使开发者使用小型、独立和通常可复用的组件构建大型应用；
- 组件化开发能大幅提高应用开发效率、测试性、复用性等；
- 组件使用按分类有：页面组件、业务组件、通用组件；
- vue的组件是基于配置的，我们通常编写的组件是组件配置而非组件，框架后续会生成其构造函数，它们基于VueComponent，扩展于Vue；
- vue中常见组件化技术有：属性prop，自定义事件，插槽等，它们主要用于组件通信、扩展等；
- 合理的划分组件，有助于提升应用性能；
- 组件应该是高内聚、低耦合的；
- 遵循单向数据流的原则

### **7.** 引进组件的步骤

答: 在template中引入组件；

在script的第一行用import引入路径；用component中写上组件名称。

### 8.函数式组件使用场景和原理

**1.定义**

函数式组件是指用一个function来渲染一个vue组件，这个组件只接受一些prop，我们将这类组件标记为functional，这意味这它**无状态**（没有响应式数据），也**没有实例**（没有this上下文和生命周期）

**函数式组件与普通组件的区别:**

1、函数式组件需要在声明组件时指定` functional:true`

2、不需要实例化，所以没有`this`，this通过render函数的第二个参数`context`代替

3、没有生命周期钩子函数，不能使用计算属性`watch`

4、不能通过$emit对外暴露事件，调用事件只能通过`context.listeners.click`的方式调用外部传入的事件

5、因为函数组件时没有实例化的，所以在外部通过ref去引用组件时，实际引用的是HTMLElement

6、函数式组件的props可以不用显示声明，所以没有在props里面声明的属性都会被自动隐式解析为prop，而普通的组件所有未声明的属性都解析到$attrs里面，并自动挂载到组件根元素上（可以通过inheritAttrs属性禁止）

**优点：**

1.由于函数组件不需要实例化，无状态，没有生命周期，所以渲染性要好于普通组件

2.函数组件结构比较简单，代码结构更清晰

**使用场景：**

假设有一个a组件，引入了 a1,a2,a3 三个组件，a组件的父组件给a组件传入了一个type属性，根据type的值a组件来决定显示 a1,a2,a3 中的哪个组件。这样的场景a组件用函数式组件是非常方便的。那么为什么要用函数式组件呢？一句话：渲染开销低，因为函数式组件只是函数。

**基本写法**

```js
 {
  functional: true,  //必须声明式一个函数式组件
  // Props 是可选的
  props: {
    // ...
  },
  // 为了弥补缺少的实例
  // 提供第二个参数作为上下文
  render: function (createElement, context) {
    // ...
  }
}

```

### 9.请说出vue.cli项目中src目录每个文件夹和文件的用法？

答：assets文件夹是放静态资源；components是放组件；router是定义路由相关的配置; app.vue是一个应用主组件；main.js是入口文件。store放置vuex的相关配置

### 10.assets和static的区别

答：**相同点**：assets和static两个都是存放静态资源文件。项目中所需要的资源文件图片，字体图标，样式文件等都可以放在这两个文件下，这是相同点

**不相同点**：

- `src/assets`中存放的静态资源文件在项目打包时，也就是运行npm run build时会将assets中放置的静态资源文件进行**压缩打包**上传，编译过程中会被webpack处理为模块依赖。因此使用assets下面的资源，在js中使用的话，路径要经过webpack中的file-loader编译，引用时需要**使用相对路径或者模块路径，**

  例如：../assets/logo.png
  而**动态引用**路径时写法：require("../assets/logo.png")

- `static`中放置的静态资源文件就**不会要走打包压缩格式化**等流程，而是直接进入打包好的目录，直接上传至服务器。
  即该目录下的资源不会被 webpack 处理，它们会被直接复制到最终的打包目录下（默认地址是 dist/static），**所以引用时需要使用绝对路径**。
  因为避免了压缩直接进行上传，在打包时会提高一定的效率，但是static中的资源文件由于没有进行压缩等操作，
  所以文件的体积也就相对于assets中打包后的文件提交较大点。在服务器中就会占据更大的空间。

**建议**：将项目中template需要的样式文件js文件等都可以放置在assets中，走打包这一流程。减少体积。而项目中引入的第三方的资源文件如bootstrap中的css文件等文件可以放置在static中，因为这些引入的第三方文件已经经过处理，我们不再需要处理，直接上传。

### 12.单页面应用和多页面应用区别及优缺点

**定义：**

- **单页面应用（SPA，Single-page Application ）**，通俗一点说就是指只有一个主页面的应用，浏览器一开始要加载所有必须的 html, js, css。所有的页面内容都包含在这个所谓的主页面中。但在写的时候，还是会分开写（页面片段），然后在交互的时候由路由程序动态载入，单页面的页面跳转，**仅刷新局部资源**。多应用于pc端。 
- **多页面（MPA，Multi-page Application ）**：就是指一个应用中有多个页面，页面跳转时是整页刷新

**优缺点：**

- 单页面的优点：用户体验好，快，内容的改变不需要重新加载整个页面，基于这一点SPA对服务器压力较小；前后端分离；页面效果会比较炫酷（比如切换页面内容时的专场动画）。 

- 单页面缺点: 不利于SEO（搜索引擎优化）；导航不可用，如果一定要导航需要自行实现前进、后退。（由于是单页面不能用浏览器的前进后退功能，所以需要自己建立堆栈管理）；初次加载时耗时多，预渲染时间长
- MPA优点：首屏加载较快，只需要加载本页面的HTML、CSS、JS；有利于SEO；页面复杂度不高，开发成本较低
- MPA缺点：网站的后期维护难度较大；页面之间的跳转受网络以及设备等影响，耗时较长，出现空白等待的页面，用户体验不高；代码重复度大，服务器压力大

**使用场景**

- SPA：适用于以操作为主，不是以展示为主的；功能较多，一个界面展示不玩；大型的后台管理系统（阿里云的管理后台）/ 功能较复杂的 WebApp（外卖）
- MPA：功能少，一个界面就能展示； 以展示为主，而非操作；分享页（微信公众号文章）

![SPA与MPAS](F:\面试相关\面试题总结\图片\SPA与MPAS.png)

### 13. vue初始化页面闪动问题

答：使用vue开发时，在vue初始化之前，由于div是不归vue管的，所以我们写的代码在还没有解析的情况下会容易出现花屏现象，看到类似于{{message}}的字样，虽然一般情况下这个时间很短暂，但是我们还是有必要让解决这个问题的。

首先：在css里加上`[v-cloak] {display: none;}`

如果没有彻底解决问题，则在根元素加上`style="display: none;"` `:style="{display: 'block'}"`

### 14.vue常用的修饰符

#### 1. 事件修饰符

​	`.stop`：等同于JavaScript中的event.stop- Propagation()，防止事件冒泡；

​	`.prevent`：等同于JavaScript中的event.- preventDefault()，阻止事件的默认行为（如果事件可取消，则取消该事件，而不停止事件的进一步传播）；

​	`.capture`：与事件冒泡的方向相反，事件捕获由外到内；

​	`.self`：只会触发自己范围内的事件，不包含子元素；

​	`.once`：只会触发一次

 `.passive`: 在监听元素滚动事件的时候，会一直触发onscroll事件让页面变的越来越卡，因此在我们使用这个修饰符后，相当于给onscroll事件增加了.lazy修饰符,

#### 2.表单修饰符

​	`.lazy`: lazy跟懒加载类似，在表单上是在我们填写信息的时候不会触发v-model值的变化，只有光标离开的时候才会赋值；

​	`.trim`: 过滤掉输入内容的前后空格

​	`.number`: 将输入的数值转为数值类型

### 15.Vue.set方法原理

答：了解 Vue 响应式原理的同学都知道在**两种情况下修改 Vue 是不会触发视图更新的**：
   1、在实例创建之后添加新的属性或者删除属性（VUE2.X中双向绑定只能识别已存在的属性，无法识别新的属性）
   2、直接更改数组下标来修改数组的值。（VUE2.X中双向绑定数组需要自行修改数组中的内容）

**Vue.set** **或者说是 $set 原理如下**

答：因为响应式数据 我们给对象和数组本身新增了__ob__属性，代表的是 Observer 实例。当给对象新增不存在的属性，首先会把新的属性进行响应式跟踪 然后会触发对象 __ob__ 的dep收集到的 watcher 去更新，当修改数组索引时我们调用数组本身的 splice 方法去更新数组。

### 16. vue中使用了哪些设计模式？

1、工厂模式 - 传入参数即可创建实例
 将new操作单独封装，遇到new时，传入不同的参数创造不同的实例

2、单例模式 - 整个程序有且仅有一个实例   

Vuex 保证唯一 Store,以及单例组件；  vue-router 的插件注册方法 install 判断如果系统存在实例就直接返回掉。

3、发布-订阅模式。（vue 事件机制，watcher订阅dep，dep通知watcher执行update）

4、观察者模式。（响应式数据原理）

>观察者模式和发布订阅者模式在概念和思想上时统一的，但是具体实现的方式不同。
>
>- 观察者模式是对象间的直接依赖，对象通知对象（外卖商家自己直接微信联系多个顾客，自己通知多个顾客可以买饭了）。
>
>- 发布-订阅者模式利用第三方平台通知订阅者发生了更新（商家通过美团平台告知顾客可以买饭了），此时，第三方平台称之为EventBus（事件总线）
>
><img src="C:\Users\SFONE\AppData\Roaming\Typora\typora-user-images\image-20220623103744693.png" alt="image-20220623103744693" style="zoom: 67%;" />

5、装饰器模式（@装饰器的用法)，是ES7提出的一个新语法，可以对类、对象、属性、方法进行修饰，对其添加一些其他的行为，旨在实现代码的复用。通俗来讲，就是对一段代码的二次包装

6、策略模式，策略模式指对象有某个行为，但是在不同的场景中，该行为有不同的实现方案 - 比如选项的合并策略。

### 17.过滤器的作用和使用方法

根据过滤器的名称，过滤器是用来过滤数据的，在Vue中使用`filters`来过滤数据，`filters`不会修改数据，而是过滤数据，改变用户看到的输出（计算属性 computed ，方法 methods 都是通过修改数据来处理数据格式的输出显示）。

**使用场景**：

- 需要格式化数据的情况，比如需要处理时间、价格等数据格式的输出 / 显示。
- 比如后端返回一个 年月日的日期字符串，前端需要展示为 多少天前 的数据格式，此时就可以用`fliters`过滤器来处理数据。

```js
//过滤器是一个函数，它会把表达式中的值始终当作函数的第一个参数。
//过滤器用在插值表达式 {{ }} 和 v-bind 表达式 中，然后放在操作符“ | ”后面进行指示。
<li>商品价格：{{item.price | filterPrice}}</li>

 filters: {
    filterPrice (price) {
      return price ? ('￥' + price) : '--'
    }
  }
```

### 18.如何保存页面当前的状态 - 持久化页面

既然是要保持页面的状态（其实也就是组件的状态），那么会出现以下两种情况：前组件会被卸载和前组件不会被卸载。

#### 1.组件会被卸载

##### 1.1 生命周期函数

只需要在组件即将被销毁的生命周期（**beforeDestory**）中在 LocalStorage / SessionStorage 中把当前组件的 state 通过 JSON.stringify() 储存下来就可以了。在这里面需要注意的是组件更新状态的时机。

比如从 B 组件跳转到 A 组件的时候，A 组件需要更新自身的状态。但是如果从别的组件跳转到 A 组件的时候，实际上是希望 A 组件重新渲染的，也就是不要从 Storage 中读取信息。所以需要在 Storage 中的状态加入一个 flag 属性，用来控制 A 组件是否读取 Storage 中的状态。

**优点**：兼容性好，不需要额外库或工具；简单快捷，基本可以满足大部分需求。

**缺点：**

- 状态通过 JSON 方法储存（相当于深拷贝），如果状态中有特殊情况（比如 Date 对象、Regexp 对象等）的时候会得到字符串而不是原来的值。（具体参考用**JSON 深拷贝的缺点**）
- 如果 B 组件后退或者下一页跳转并不是前组件，那么 flag 判断会失效，导致从其他页面进入 A 组件页面时 A 组件会重新读取 Storage，会造成很奇怪的现象

>JSON深拷贝的缺点：
>
>1. 不会拷贝对象上的value值为undefined和函数的键值对
>2. nan，无穷大，无穷小会转为null
>3. 将constructor强行转为Object
>4. 无法获取自己原型链上的内容，只能获取Object原型内容
>5. :date对象经过序列化会变成date字符串

##### 1.2 路由独享守卫

监听离开页面的时机用：beforeRouteLeave，存储用localStorage或vuex。独享导航守卫，它可以监听该组件页面路由跳转的时机，我们就可以在这个时机做我们想做的事情，写的时候和methods同级。

##### 1.3 vuex插件-persistedState插件

```js
npm install vuex-persistedstate -S //安装插件

//2. 在 store/index.js 文件中添加以下代码：
import persistedState from 'vuex-persistedstate'
const store = new Vuex.Store({
 state:{},
 getters:{},
 ...
 plugins: [persistedState()] //添加插件
})

//使用sessionStorage进行存储，修改pugins中的代码
plugins: [
    persistedState({ storage: window.sessionStorage })
]

```

#### 2.组件不会被卸载

##### 2.1 keep-alive

当组件在keep-alive内被切换时组件的activated、deactivated这两个生命周期钩子函数会被执行
被包裹在keep-alive中的组件的状态将会被保留：

```html
<keep-alive>
	<router-view v-if="$route.meta.keepAlive"></router-view>
</kepp-alive>

//router.js
{
  path: '/',
  name: 'xxx',
  component: ()=>import('../src/views/xxx.vue'),
  meta:{
    keepAlive: true // 需要被缓存
	
  }
},
```

### 19. VUE 的模板编译原理

>**template:** 是 Vue 提供的类html语法，用来书写页面结构，可以在上面写html、指令、插值和 js 表达式，语法易于理解，书写简单，但缺点是不够灵活。主要应用于vue
>
>```html
><h1 v-if="level === 1">
><slot></slot>                   //template使用插槽的形式
></h1>
><h2 v-if="level === 2">
><slot></slot>
></h2>
><h3 v-if="level === 3">
><slot></slot>
></h3>
><h4 v-if="level === 4">
><slot></slot>
></h4>
><h5 v-if="level === 5">
><slot></slot>
></h5>
><h6 v-if="level === 6">
><slot></slot>
></h6>
>```
>
>**render:** 是 Vue 提供的另一种书写页面的方式，Vue 除了可以用 template 写页面，也可以用 render 函数结合 `createElement` 方法或者 `JSX` 书写页面，render 函数比 template 更接近编译器。
>
>```js
>props: {
>level: {
>type: Number,
>default: 1
>}
>},
>render(createElement) {
>return createElement('h' + this.level, this.$slots.default)           //render形式
>}
>
>
>//在入口文件main.js中，会使用render直接渲染整个APP文件
>new Vue({
>  router,
>  store,
>  render: h => h(App),      //使用h函数生成APP的虚拟文件并渲染
>  beforeCreate() {
>    Vue.prototype.$bus = this //安装全局事件总线
>  }
>}).$mount('#app')
>```
>
>**createElement**: createElement 是 Vue 提供的一个函数，可以通过传入 `tag`(元素名)、`data`(属性)和 `children`(子元素) 这三个参数，来生成一个 `VNode`。( 例，createElement( 'h' + , 2，23333)  or createElement(‘h1’,’233333’) )    //创建一个h2标签，里面包含文本233333
>
>**JSX:**  JSX 是一个 JavaScript 的语法扩展，可以很好地描述 UI 应该呈现出它应有交互的本质形式，并且具有 JavaScript 的全部功能，十分灵活。主要应用于react
>
>```jsx
>props: {
>level: {
>type: Number,
>default: 1
>}
>},
>render() {
>const Tag = `h${this.level}`
>return <Tag>{this.$slots.default}</Tag>             // JSX的形式，vue-cli 3.0版本以上自动支持 JSX
>}
>```

>AST(抽象语法树）：利用 抽象语法树(AST) 可以对你的源代码进行修改、优化，甚至可以打造自己的编译工具。其实有点类似babel的功能。本质上是一个json对象

Vue中的模板template无法被浏览器解析并渲染，因为这不属于浏览器的标准，不是正确的HTML语法，所以需要将template转化成一个JavaScript函数，这样浏览器就可以执行这一个函数并渲染出对应的HTML元素，就可以让视图跑起来了，这一个转化的过程，就成为模板编译。模板编译又分三个阶段，解析parse，优化optimize，生成generate，最终生成可执行函数render。可以总结成以下几步：

1. 调用parse方法 解析template模板字符串: 这个过程使用了大量的正则表达式对template字符串进行解析，将标签、指令、属性等转换为抽象语法树（AST）`const ast = parse(template.trim(), options)`。

   >- parse的目标：把tamplate转换为AST树，它是一种用 JavaScript对象的形式来描述整个模板。
   >
   >- 解析过程：利用正则表达式顺序解析模板，当解析到开始标签、闭合标签、文本的时候都会分别执行对应的 回调函数，来达到构造AST树的目的
   >- AST元素节点总共三种类型：type为1表示普通元素、2为表达式、3为纯文本

2. 优化AST，方便后续虚拟DOM更新     `optimize(ast, options)`

   >深度遍历AST，查看每个子树的节点元素是否为静态节点或者静态节点根。如果为静态节点，他们生成的DOM永远不会改变，这对运行时模板更新起到了极大的优化作用。这个过程主要分析出哪些是静态节点，给其打一个标记，为后续更新渲染可以直接跳过静态节点做优化
   
3. 将AST转化为可执行代码=》render字符串  `const code = generate(ast, options)`

   >generate将AST抽象语法树编译成 render字符串, 使用with(this)改变作用域，最后通过`return new Function(render) `生成render字符串。

4. 执行render转化为Vnode, 并生成一个虚拟DOM

   >在源码中查看render function字符串，发现有大量的`_c`,`_v`,`_s`,`_q`
   >
   >```js
   >/*处理v-once的渲染函数*/
   >  Vue.prototype._o = markOnce
   >  /*将字符串转化为数字，如果转换失败会返回原字符串*/
   >  Vue.prototype._n = toNumber
   >  /*将val转化成字符串*/
   >  Vue.prototype._s = toString
   >  /*处理v-for列表渲染*/
   >  Vue.prototype._l = renderList
   >  /*处理slot的渲染*/
   >  Vue.prototype._t = renderSlot
   >  /*检测两个变量是否相等*/
   >  Vue.prototype._q = looseEqual
   >  /*检测arr数组中是否包含与val变量相等的项*/
   >  Vue.prototype._i = looseIndexOf
   >  /*处理static树的渲染*/
   >  Vue.prototype._m = renderStatic
   >  /*处理filters*/
   >  Vue.prototype._f = resolveFilter
   >  /*从config配置中检查eventKeyCode是否存在*/
   >  Vue.prototype._k = checkKeyCodes
   >  /*合并v-bind指令到VNode中*/
   >  Vue.prototype._b = bindObjectProps
   >  /*创建一个文本节点*/
   >  Vue.prototype._v = createTextVNode
   >  /*创建一个空VNode节点*/
   >  Vue.prototype._e = createEmptyVNode
   >  /*处理ScopedSlots*/
   >  Vue.prototype._u = resolveScopedSlots
   >
   >  /*创建VNode节点*/
   >  vm._c = (a, b, c, d) => createElement(vm, a, b, c, d, false)
   >//其他的下划线方法在 core/instance/render-helpers 中都有定义，每个方法具体做了什么不做展开。
   >
   >```
   >
   >通过这些函数，render函数最后会返回一个VNode节点，在_update的时候，经过patch与之前的VNode节点进行比较，得出差异后将这些差异渲染到真实的DOM上。

5. diff算法更新虚拟DOM

6. 产生、更新真实节点

### 20. template和jsx有什么区别

jsx特点：

- 以使用完整的编程语言 JavaScript 功能来构建你的视图页面。比如你可以使用临时变量、JS 自带的流程控制、以及直接引用当前 JS 作用域中的值等等。
- 更偏重逻辑的处理。
- 更细粒度的控制交互细节，比如：使用一个首字母大写的变量，HTML标签可动态生成。

Template特点：

- 写法贴近HTML，是官方推荐的写法
- 主要用于快速构建页面，不方便写入较复杂的逻辑处理。
- 使用上更局限于vue本身的指令api，无法做到编码随心所欲。

**使用场景：**动态的生成标题标签

```js
//---------------------------------------------template实现-----------------------------------------------
<h1 v-if="level === 1">
    <slot></slot>
  </h1>
  <h2 v-else-if="level === 2">    // 存在大量重复代码
    <slot></slot>
  </h2>
  <h3 v-else-if="level === 3">
    <slot></slot>
  </h3>
  <h4 v-else-if="level === 4">
    <slot></slot>
  </h4>
  <h5 v-else-if="level === 5">
    <slot></slot>
  </h5>
  <h6 v-else-if="level === 6">
    <slot></slot>
  </h6>

//---------------------------------------------	jsx实现-----------------------------------------------
<script>
export default {
  name: 'Child',
  data () {
    return {
      num: 1
    }
  },
  methods: {
  },
  computed: {},
  mounted () {},
  render () {
    const H = 'h' + this.num // 动态控制变量num就行了
    return <H>{ this.$slots.default }</H>
  }
}
</script>
<style scoped lang="less">
</style>

```

### 21.template中的this指向

#### 1.为什么vue组件中可以使用this访问到data和methods中的内容？

- 在VUE源码文件 initMethods中，在vue实例上定义了边methods中所有的方法，并使用bind函数将函数的this指向Vue实例上

`  vm[key] = typeof methods[key] !== 'function' ? noop : bind(methods[key], vm);`

- `methods`里的方法通过 `bind` 指定了`this`为 new Vue的实例(`vm`)，methods里的函数也都定义在`vm`上了，所以可以直接通过`this`直接访问到`methods`里面的函数。

- `data`函数返回的数据对象也都存储在了new Vue的实例(`vm`)上的`_data`上了，访问 `this.name`时实际访问的是`Object.defineProperty`代理后的 `this._data.name`。

VUE在模板编辑过过程中，有一个步骤是使用`generate`将优化后的`AST`转换为render字符串, 在转换后，会使用with方法，改变作用域，让this指向当前vue实例？？？

#### 2.vue组件中出现的this混淆问题

在Vue所有的[生命周期](https://so.csdn.net/so/search?q=生命周期&spm=1001.2101.3001.7020)钩子方法（如created，mounted， updated以及destroyed）里使用this，this指向调用它的Vue实例。但是有几种特殊情况：

**在Vue实例中：**

- methods中如果用的是正常函数，那么它的this就指向Vue实例；

- 如果是箭头函数，this就指向window对象。 

 **Vue 中回调函数中的 this：**

1. 若回调函数为**匿名函数**，非严格模式下指向 window,严格模式下为 undefined。
2. 若回调函数为自定义方法，则 this 指向 Vue 实例。
3. 若回调函数为 箭头函数，则 this 指向 Vue 实例。

```js
<div id="app" style="width: 100%;height: auto;font-size:20px;">
    <p id="id1"></p>
    <p id="id2"></p>
    <p id="id3"></p>
    <p id="id4"></p>
</div>

//----------------------------------------------------------------------------------------------------------------------------
<script type="text/javascript">
    var message = "Hello!";
    var app = new Vue({
        el:"#app",
        data:{
            message: "你好！"
        },
        created: function() {
            this.showMessage1();
            this.showMessage2();
            this.showMessage3();
            this.callC()  
        },
        methods:{
//------------在Vue实例中，methods中如果用的是正常函数，那么它的this就指向Vue实例；如果是箭头函数，this就指向window对象。---------------------
            callb:function(){   //你好 -VUE实例
                document.getElementById("id3").innerText = 'id3' + this.message;  //
            },
            callC:()=>{    //  hello  -Vwindows对象
                document.getElementById("id4").innerText = 'id4' + this.message;  //
            },

   //------------------在VUE回调函数中，如果回调函数是箭头函数或自定义方法，指向VUE实例，如果回调函数是匿名函数，指向windows
            showMessage1:function(){
                setTimeout(function() {  //Hello
                    document.getElementById("id1").innerText = 'id1' + this.message;
                }, 10)
            },
            showMessage2:function() {
                setTimeout(() => {   //你好
                    document.getElementById("id2").innerText = 'id2' + this.message;
                }, 10)
            },
            showMessage3:function () {
               setTimeout(this.callb,100)
            },

        }
    });
```

#### 3.修改vue中的this

接着上述的例子：

```js
showMessage1:function(){
    setTimeout(function() {
       document.getElementById("id1").innerText = this.message;  //this 3
    }.bind(this), 10)
}   //setTimeout()里的匿名函数使用bind()绑定到vue实例的this。这样在匿名函数内的this也为vue实例。

```

### 22. Vue中的DOM更新机制与$nextTick

#### 1.DOM更新机制

Vue中的数据是异步更新的，这意味这我们**在修改Vue.data之后并不能立刻获取修改后的DOM元素并触发页面更新**，只能在`$nextTick`回调中获取。VUE官方文档中说：

>Vue异步执行DOM更新。只要观察到数据变化，Vue将开启一个**队列**，并缓冲在同一事件循环中发生的所有数据改变。如果同一个watcher被多次触发，只会被推入到队列中一次。这种在缓冲时去除重复数据对于避免不必要的计算和DOM操作上非常重要。然后，在下一个的事件循环“tick”中，Vue刷新队列并执行实际 (已去重的) 工作。
>
>**为什么VUE是异步渲染的？**
>
>为如果不采用异步更新，那么每次更新数据都会对当前组件进行重新渲染，所以为了性能考虑，Vue会在本轮数据更新后，再去异步更新数据。具体实现方法：**在事件循环中，微任务会先于宏任务执行。而在微任务执行完后会进入浏览器更新渲染阶段，所以在更新渲染前使用微任务会比宏任务快一些，一次循环就是一次tick 。（页面渲染也是一个宏任务）**在一次event loop中，微任务在这一次循环中是一直取一直取，直到清空微任务队列，而宏任务则是一次循环取一次。

**白话：**因为Vue处于性能考虑，Vue会将用户同步修改的多次数据缓存起来，等同步代码执行完，说明这一次的数据修改就结束了，然后才会去更新对应DOM，一方面可以省去不必要的DOM操作，比如同时修改一个数据多次，只需要关心最后一次就好了，另一方面可以将DOM操作聚集，提升render性能。

https://juejin.cn/post/7089980191329484830（VUE异步更新DOM原理）

#### 2.$nextTick

**定义：**nextTick的**目的就是产生一个回调函数加入微任务（使用promise.then或MutationObserve的形式）或者宏任务（若存在兼容问题，则使用setTimeOut的方式）中，当前栈执行完以后（可能中间还有别的排在前面的函数）调用该回调函数，起到了异步触发（即下一个事件循环-tick时触发）的目的**。

放在`$nextTick`中的操作不会立即执行，而是等数据更新、DOM更新完成之后再执行，此时就可以拿到最新的数据。`$nextTick`返回一个promise对象，将回调延迟到下次DOM更新循环之后执行。在VUE源码中，VUE尝试异步队列采用原生的Promise.then、MutationObserver（微任务）和setImmediate, 如果执行环节不支持，则采用setTimeout代替。该方法是典型的利用JS的异步回调任务队列，来实现自己的异步回调队列。

**使用场景：**

1. created中获取DOM的操作需要使用它
2. **页面使用了Vue的某个变量，希望在变量更新后立即操作变量映射的dom，但是发现查询到的dom信息是更新之前的, 这是因为VUE中的事件更新机制（真实dom渲染和数据是异步的）。我们可以把希望在真实dom更新完成后立即执行的东西放在$nextTick中**
3. 还有一些第三方插件使用过程中，使用到的情况，具体问题具体分析

```js
// $nextTick可以这样用
createApp({
  // ...
  methods: {
    // ...
    example() {
      // 修改数据
      this.message = 'changed'
      // DOM 尚未更新
      this.$nextTick(function() {                //不要在$nextTick中写任何引发DOM改变的操作，容易陷入死循环
        // DOM 现在更新了
        // `this` 被绑定到当前实例
        this.doSomethingElse()
      })
    }
  }
})

//因为 $nextTick() 返回一个 Promise 对象，所以你可以使用新的 ES2017 async/await 语法完成相同的事情
methods: {
  updateMessage: async function () {
    this.message = '已更新'
    console.log(this.$el.textContent) // => '未更新'
    await this.$nextTick()
    console.log(this.$el.textContent) // => '已更新'
  }
}
```

### 23.简述mixins、extend、extends

#### 1. Mixins

>**官方定义：**混入 (mixins) 提供了一种非常灵活的方式，来**分发 Vue 组件中的可复用功能**。一个混入对象可以包含任意组件选项。当组件使用混入对象时，所有混入对象的选项将被“混合”进入该组件本身的选项。
>
>**民间解释：**将**组件的公共逻辑或者配置提取出来**，哪个组件需要用到时，直接将提取的这部分混入到组件内部即可。这样既可以减少代码冗余度，也可以让后期维护起来更加容易。（**提取的是逻辑或配置，而不是HTML代码和CSS代码。**）
>
>**和VUEX的区别:**如果在一个组件中更改了vuex中的某个数据，那么其他组件也会受到影响，牵一发而动全身。Mixin中的数据和方法都是独立的，组件之间不互相影响

**使用方法：**

mixin是一个对象，可以包括vue组件中常见的配置，包括data，methods，created等。一般在src目录中新建mixin文件夹，在里面新建index.js文件

```js
// src/mixin/index.js
export const mixins = {
  data() {
    return {};
  },
  computed: {},
  created() {},
  mounted() {},
  methods: {},
};

//全局使用mixin，在main.js中修改(不推荐全局使用mixin)
import Vue from "vue";
import App from "./App.vue";
import { mixins } from "./mixin/index";
Vue.mixin(mixins);

Vue.config.productionTip = false;

new Vue({
  render: (h) => h(App),
}).$mount("#app");


//在App.vue组件中局部使用
// src/App.vue
<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png" />
    <button @click="clickMe">点击我</button>
  </div>
</template>

<script>
import { mixins } from "./mixin/index";      //引入的是mixins对象
export default {
  name: "App",
  mixins: [mixins],    //在mixins属性中引入定义好的mixins数组，只能接受数组形式，可以继承多个，相当于多继承
  components: {},
  created(){
    console.log("组件调用minxi数据",this.msg);
  },
  mounted(){
    console.log("我是组件的mounted生命周期函数")
  }
};
</script>


```

**注意：**

1.生命周期函数冲突

- mixin中的生命周期函数会和组件的生命周期函数一起合并执行。
- mixin中的data数据在组件中也可以使用。
- mixin中的方法在组件内部可以直接调用。
- 生命周期函数合并后执行顺序：先执行mixin中的，后执行组件的。

2.data数据冲突

当mixin中的data数据与组件中的data数据冲突时，组件中的data数据会覆盖mixin中数据 

```js
var mixin = {
  data: function () {
    return {
      message: 'hello',
      foo: 'abc'
    }
  }
}

new Vue({
  mixins: [mixin],
  data: function () {
    return {
      message: 'goodbye',
      bar: 'def'
    }
  },
  created: function () {
    console.log(this.$data)
    // => { message: "goodbye", foo: "abc", bar: "def" }
  }
})

```

3.方法冲突

- 这种冲突很容易遇到，毕竟大家命名方法的名字很容易一样。实际上最终调用的是组件中的方法，而不是mixin中的方法

**优缺点：**

优点：

- 提高代码复用性
- 无需传递状态
- 维护方便，只需要修改一个地方即可

缺点：

- 命名冲突
- mixin之间不能传递状态
- 滥用的话后期很难维护
- 逻辑来源没有清晰的说明，不好追溯源，排查问题稍显麻烦
- 不能轻易的重复代码

#### 2. vue.extend（vue3中已经移除）

> vue-extend创建的是一个**组件构造器**，而不是一个具体的实例
>
> **使用场景: **在使用vue开发的一般都是单页面应用，每个页面（组件）的模板都是提前写好的并且是固定的，然后通过路由来控制页面的跳转。并且整个应用只有一个根节点`#app`，所有的内容都是挂在这个`#app`节点中的。但是有时候由于业务需要我们可能要去**动态的生成一个组件**并且要**独立渲染到其它元素节点**中,这个时候Vue.extend和vm.$mount就派上用场了。(弹窗)
>
> extend解决了以下问题：
>
> 1. 组件模板都是事先定义好的，如果我要从接口动态渲染组件怎么办？
> 2. 所有内容都是在 #app 下渲染，注册组件都是在当前位置渲染。如果我要实现一个类似于 window.alert() 提示组件要求像调用 JS 函数一样调用它，该怎么办？

**使用方法：**

```js
<div id="mount-point"></div>
// 创建构造器
var Profile = Vue.extend({      
  template: '<p>{{firstName}} {{lastName}} aka {{alias}}</p>',    //创造组件模板
  data: function () {
    return {
      firstName: 'Walter',
      lastName: 'White',
      alias: 'Heisenberg'
    }
  }
})
// 创建 Profile 实例，并挂载到一个元素上。
new Profile().$mount('#mount-point')

// 结果如下：
<p>Walter White aka Heisenberg</p>
```

#### 3. extends（继承）

**理解**

**使用方法：**

```js
//A组件methods中有一个方法，直接输出val
methods:{
     componentAHandler(val) {
         console.log(val)
     },
}

import A from './A'
const B = {
    name: 'B',
    extends: A,               //B组件继承A组件，接收参数是一个对象或者构造函数(JS是万物基于Object， 这表示即使是Vue.component也是一个Object)，相当于一个单继承
    methods: {
        componentAHandler(val) {
            this.processByOther(val)   //B组件重写A组件中的内容，在输出val之前调用了另一个函数
            console.log(val)
        },
    }
}
```

#### 4. mixin和extends的覆盖逻辑

mixin 和 extends均是用于合并、拓展组件的，两者均通过 mergeOptions (parent,child,vm)（选项合并过程，参数表示将child中的内容合并至parent中）方法实现合并。

- mixins 接收一个混入对象的**数组**，其中混入对象可以像正常的实例对象一样包含实例选项，这些选项会被合并到最终的选项中。Mixin 钩子按照传入顺序依次调用，并在调用组件自身的钩子之前被调用。
- extends 主要是为了便于扩展单文件组件，继承一个**对象或构造函数**。
- mixins和extends都可以理解为继承。 mixins接受的是一个数组可以理解为面相对象语言的**多继承**，extends接受的是一个对象或函数，可以理解为**单继承**；

![img](https://cdn.nlark.com/yuque/0/2021/jpeg/1500604/1609518480272-8cb1af01-a4a8-4d54-91bb-5546aafac510.jpeg)

## 二、虚拟DOM

数据改变 -> 虚拟DOM (计算变更) -> 操作真实DOM -> 视图更新 

>“软件开发中遇到的所有问题都可以通过增加一层抽象而得以解决。DOM效率低下的这个问题同样可以通过增加一层抽象解决。虚拟DOM就是这层抽象，建立在真实DOM之上，对真实DOM的抽象”。

### 0.虚拟DOM

**背景：**在DOM节点多的情况下，操作DOM会拖慢页面性能，而前端工作的视图更新和状态维护都需要DOM操作。`jQuery`可以利用元素选择器及高度封装的API实现对DOM的高效操作。而MVVM的发展让数据可以双向绑定，我们不需要操作DOM元素，数据会让视图状态自行更新。

**原生操作dom的缺点**：我们传统的开发模式，原生JS或JQ操作DOM时，浏览器会从构建DOM树开始从头到尾执行一遍流程。在一次操作中，我需要更新10个DOM节点，浏览器收到第一个DOM请求后并不知道还有9次更新操作，因此会马上执行流程，最终执行10次。例如，第一次计算完，紧接着下一个DOM更新请求，这个节点的坐标值就变了，前一次计算为无用功。计算DOM节点坐标值等都是白白浪费的性能。即使计算机硬件一直在迭代更新，操作DOM的代价仍旧是昂贵的，频繁操作还是会出现页面卡顿，影响用户体验。操作DOM不可避免的会出现重排（占用、消耗CPU）；重排则会占用、消耗GPU。

**理解虚拟DOM：**相对于原生DOM，js对象处理的速度更快，而DOM树的元素可以抽象为js对象，主要包含了 `tag`、`props`、`children` 三个属性，如下：

```js
<ul id='list'>
  <li class='item'>Item 1</li>
  <li class='item'>Item 2</li>
  <li class='item'>Item 3</li>
</ul>
-------------------------------------虚拟DOM表示-----------------------------------
var element = {
  tagName: 'ul', // 节点标签名
  props: { // DOM的属性，用一个对象存储键值对
    id: 'list'
  },
  children: [ // 该节点的子节点
    {tagName: 'li', props: {class: 'item'}, children: ["Item 1"]},   
    {tagName: 'li', props: {class: 'item'}, children: ["Item 2"]},
    {tagName: 'li', props: {class: 'item'}, children: ["Item 3"]},
  ]
}

```

反之，也可以用js对象表示一颗真正的DOM树。若一次操作中有 10 次更新 `DOM` 的动作，虚拟 `DOM` 不会立即操作 `DOM`，而是将这 10 次更新的 `diff` 内容保存到本地一个 `JS` 对象中，最终将这个 `JS` 对象一次性 `attch` 到 `DOM` 树上，再进行后续操作，避免大量无谓的计算量。**这表示当状态变更时，我们可以重新渲染JS对象结构，记录新的对象结构和旧的对象结构之间的差异，按照差异操作真实的DOM树，让页面更新**。这样的优点是显而易见的，我们只修改了发生变化的DOM节点，而不是重新渲染，极大的节省了性能。这就是传说的Virtual DOM算法：

>diff算法 — 调用名为patch的函数，比较两棵虚拟DOM树的差异，一边比较一边给真实的DOM打补丁
>
>`diff` 是发生在虚拟 `DOM` 上的：新虚拟 `DOM` 和老虚拟 `DOM` 进行 `diff` (精细化比较), 算出应该如何最小量更新，最后反映到真实的 `DOM` 上

**虚拟DOM的解析过程：**

- 首先对将要插入到文档中的 DOM 树结构进行分析，使用 js 对象将其表示出来，比如一个元素对象，包含 TagName、props 和 Children 这些属性（上述工作一般在snabbdom中的**h函数， Vue 中的 render 方法中的 `createElement`进**行）。然后将这个 js 对象树给保存下来，最后再将 DOM 片段插入到文档中。
- 当页面的状态发生改变，需要对页面的 DOM 的结构进行调整的时候，首先根据变更的状态，重新构建起一棵对象树，然后将这棵新的对象树和旧的对象树进行比较，记录下两棵树的的差异。(patch函数中的diff )
- 最后将记录的有差异的地方应用到真正的 DOM 树中去，这样视图就更新了。

### 1.虚拟 DOM 的优缺点？ 

答：虚拟DOM是指**用JS对象模拟DOM结构**，一个能代表DOM树的对象，通常含有标签名、标签上的属性、事件监听和子元素们以及其他属性，真实DOM的一切属性都在虚拟DOM中有对应的属性。Vue中的虚拟DOM参考的是Snabbdom。

>Snabbdom: 源于瑞典语，意为“速度”，是著名的虚拟 `DOM` 库，是 `diff` 算法的鼻祖，`Vue` 源码就是借鉴了 `snabbdom`

**虚拟DOM比真实DOM快的原因有以下几点**：

- 减少DOM操作：虚拟DOM可以将多次操作合并为一次操作，比如添加1000个节点，真实DOM需要添加1000次，而虚拟DOM只需要1次添加一次，指**优化了操作次数**

- 虚拟DOM可以借助diff算法，将多余操作省掉，比如添加1000个节点，只有10个是新增的，虚拟DOM可以识别是否更新节点，只更新发生变化的dom节点，**优化了操作范围**

- 虚拟DOM本质上是 JavaScript 对象，可以**跨平台**，变成小程序、ios应用、安卓应用等

- **无需手动操作 DOM**：我们不再需要手动去操作 DOM，只需要写好 View-Model 的代码逻辑，框架会根据虚拟 DOM 和 数据双向绑定，帮我们以可预期的方式更新视图，极大提高我们的开发效率；

- **保证性能下限**：框架的虚拟 DOM 需要适配任何上层 API 可能产生的操作，它的一些 DOM 操作的实现必须是普适的，所以它的性能并不是最优的；但是比起粗暴的 DOM 操作性能要好很多，因此框架的虚拟 DOM 至少可以保证在你不需要手动优化的情况下，依然可以提供还不错的性能，即保证性能的下限；

  >- 真实DOM∶ 生成HTML字符串＋重建所有的DOM元素
  >- 虚拟DOM∶ 生成vNode+ DOMDiff＋必要的dom更新

**缺点:**

- 无法进行极致优化：虽然虚拟DOM 合理的优化，足以应对绝大部分应用的性能需求，但在一些性能要求极高的应用中虚拟 DOM 无法进行针对性的极致优化。且DOM需要额外的创建函数创建虚拟DOM，如createElement或h(VUE中的render), 但可@以使用JSX简化创建虚拟DOM：

```js
//VUE使用vue-loader转化为h形式
<div class="red" @click="fn">
	<span> span1 </span>
	<span> span2 </span>
</div>
```

​		这种JSX的缺点是严重依赖打包工具，添加额外的构建过程，否则js不认上述代码

- 首次渲染大量DOM时，由于多了一层虚拟DOM的计算，会比innerHTML插入慢。但是正如它能保证性能下限，在真实DOM操作的时候进行针对性的优化时，还是更快的。

### 2. h函数

>虚拟节点的相关属性：
>
>```js
>{
>  children: undefined, // 子节点，undefined表示没有子节点
>  data: {}, // 属性样式等
>  elm: undefined, // 该元素对应的真正的DOM节点，undefined表示它还没有上树
>  key: undefined, // 节点唯一标识
>  sel: 'div', // selector选择器 节点类型（现在它是一个div）
>  text: '我是一个盒子' // 文字
>}
>
>```

h函数用于产生虚拟节点（vnode），使用方法如下：

```js
const vir = h('a', { props: { href: 'http://www.atguigu.com' } }, '尚硅谷')   //产生虚拟节点

//console.log(vir)的结果如下
{ "sel": "a", "data": { "props": { "href": "http://www.atguigu.com" } }, "text": "尚硅谷" }   //得到的虚拟节点

//让虚拟节点上树
const container = doucment.getElementById('container')
patch(container, vir)

//此时页面成功渲染出a标签
<a href="http://www.atguigu.com">尚硅谷</a>  //真正表示的DOM元素

```

h函数支持嵌套使用

```js
h('ul', {}, [
  h('li', {}, '牛奶'),
  h('li', {}, '咖啡'),
  h('li', {}, '可乐')
])

//产生的虚拟DOM树
{
  "sel": "ul",
  "data": {},
  "children": [
    { "sel": "li", "data": {}, "text": "牛奶" },
    { "sel": "li", "data": {}, "text": "咖啡" },
    { "sel": "li", "data": {}, "text": "可乐" }
  ]
}
```



### 3. diff算法

<img src="C:\Users\SFONE\AppData\Roaming\Typora\typora-user-images\image-20220615153548507.png" alt="image-20220615153548507" style="zoom:67%;" />

#### 3.1 流程

diff处理新旧节点：

<img src="F:\面试相关\面试题总结\图片\patch函数.png" alt="patch函数" style="zoom: 67%;" />

#### 3.2 diff的优化更新策略

Diff有三大策略：

Tree Diff：是对树每一层进行遍历，找出不同     

Component Diff：是数据层面的差异比较    

Element Diff ：真实DOM渲染，结构差异的比较

新前、新后，旧前，旧后均为指针类型，下述情况命中一种就不再继续判断了：

- 新前与旧前
- 新后与旧后
- 新后与旧前（`此种命中，涉及移动节点，那么旧前指向的节点，移动到旧后之后`）
- 新前与旧后（`此种命中，涉及移动节点，那么旧后指向的节点，移动到旧前之前`）

while( 新前 <= 新后 && 旧前 <= 旧后 ){}

- 如果是旧节点先循环完毕，说明新节点中有要插入的节点 
- 如果新节点先循环完毕，老节点中还有剩余节点，则表明有要删除的节点

#### 3.3 常见的问题

- key很重要：需要使用key来给每个节点做一个唯一标识，Diff算法就可以正确的识 别此节点。如果不加key，可能会全部更新，这也是v-for必须加key的原因。加上key之后，只会更新改变量。作用主要是为了高效的更新虚拟DOM。

- 只有是同一个虚拟节点，才会精细化比较（最小量更新），否则就是暴力删除旧的，插入新的。（同一个虚拟节点必须选择器相同且key相同）

  >```js
  >const vnode1= h('ul',{},[
  >	h{'li',{key:'A'},'A'},
  >	h{'li',{key:'B'},'B'},
  >	h{'li',{key:'C'},'C'},
  >])
  >
  >const vnode2= h('ol',{},[
  >	h{'li',{key:'A'},'A'},
  >	h{'li',{key:'B'},'B'},
  >	h{'li',{key:'C'},'C'},
  >])
  >```
  >
  >此时vnode1和vnode2不是同一个虚拟节点，他们的’ul‘ 标签和’ol‘标签不一致，导致内部的`li`标签被暴力拆除（尽管`li`标签的内容和key都是一致的，但是他们的父节点不一样，仍要暴力拆除）

- 在前端中，diff算法只会对统一级别的元素比较，不会跨层比较。发现跨层直接暴力拆除，重新构建，所以diff算法的时间复杂度是O(n)

### 4. diff算法

diff的过程就是调用名为`patch`的函数，比较新旧节点，一边比较一边给**真实的DOM**打补丁。Patch函数一直递归调用，直到遇见文本节点，一层一层往回调

在采取diff算法比较新旧节点的时候，比较只会在同层级进行, 不会跨层级比较。

<img src="C:\Users\SFONE\AppData\Roaming\Typora\typora-user-images\image-20220308194913244.png" alt="image-20220308194913244" style="zoom: 80%;" /><img src="C:\Users\SFONE\AppData\Roaming\Typora\typora-user-images\image-20220308200416450.png" alt="image-20220308200416450"  />

**过程：**

patches= patch( oldVNode, newVNode)  	    温馨提示：`VNode`和`oldVNode`都是对象，一定要记住）

patches是要运行的DOM操作，判断两个节点是否值得比较，值得比较则执行patchVnode方法，不值得比较则用Vnode替换oldVnode

patchVnode函数做了以下事情：

- 找到对应的真实dom，称为`el`
- 判断`Vnode`和`oldVnode`是否指向同一个对象，如果是，那么直接`return`
- 如果他们都有文本节点并且不相等，那么将`el`的文本节点设置为`Vnode`的文本节点。
- 如果`oldVnode`有子节点而`Vnode`没有，则删除`el`的子节点
- 如果`oldVnode`没有子节点而`Vnode`有，则将`Vnode`的子节点真实化之后添加到`el`
- 如果两者都有子节点，则执行`updateChildren`函数比较子节点，这一步很重要

**缺点：**如果不使用key，diff会使用一种最大限度减少动态元素并且尽可能的尝试就地修改/复用相同类型元素。如果不设置key，同级比较会出现bug，**主要问题在于数组下标index不可靠**，在table表单里，默认在diff阶段复用顶部元素，在末尾append一个tr元素。计算机逻辑问题。破解方法：加上key标识（id标识）

**时间复杂度：**

- 传统的Diff算法是通过遍历循环对比新的虚拟DOM与之前保存的旧的虚拟DOM之间的变化，如果有变化，还要在更新（两层嵌套加上更新节点，时间复杂度为-O（n^3））
- VUE中的diff算法：因为在前端中，很少会跨域层级的移动DOM元素，所以Vritual Dom只会对同一个层级的元素进行对比，这样算法复杂度是O（n）

### 5. Vue中key的作用

>Diffing算法我们大概都知道，就是将新虚拟DOM与旧虚拟DOM进行比较，如果每一个虚拟DOM都没有自己的“身份证号”，那么在进行新旧虚拟DOM比较的时候，就很难确定新旧虚拟DOM是否相同、以及新旧虚拟DOM中的内容是否相同，而如果每一个虚拟DOM都有一个属于自己的“身份证号”，那么比较的时候我们只需要根据“身份证号”就可以知道新旧虚拟DOM是否相同了，这样一来，Diffing算法的效率也因此提升了，而这个“身份证号”就是虚拟DOM对象的标识——key

vue 中 key 值的作用可以分为三种情况来考虑：

1.  **v-if 中使用 key**。由于 Vue 会尽可能高效地渲染元素，通常会**复用已有元素而不是从头开始渲染**。我们在vue中如果使用`v-if`进行切换时，此时`Vue`为了更加高效的渲染，此时会进行前后比较，如果切换前后都存在的元素，则直接复用。特殊情况：如果我们在模板中切换前后都存在`input`框，此时我们在`input`框中写入一些数据，并且进行页面切换，则原有的数据就会保存。此时我们就可以使用`key`，给每一个`input`框，添加一个唯一的标识`key`，来表示元素的唯一性，做到input中元素内容不保留
2. **v-for 中使用 key**。对于用`v-for`渲染的列表数据来说，数据量可能一般很庞大，而且我们经常还要对这个数据进行一些增删改操作。那么整个列表都要重新进行渲染一遍，那样就会很费事。而`key`的出现就尽可能的回避这个问题，提高效率。`v-for`默认使用就地复用的策略，列表数据修改的时候，他会根据`key`值去判断某一个值是否修改，如果修改则重新渲染该项，否则复用之前的元素。在`v-for`中我们的`key`一般为`id`，也就是唯一的值，但是一般不要使用`index`作为key。
3. **diff中使用key**。key 是为 Vue 中 vnode 的唯一标记，通过这个 key，diff 操作可以更准确、更快速的**判断两个节点是否是同一个**，从而避免频繁的更新不同元素，让整个patch过程更加高效，减少DOM操作量，提升性能
   - 更准确：因为带 key 就不是就地复用了，在 sameNode 函数a.key === b.key对比中可以避免就地复用的情况。所以会更加准确。
   - 更快速：利用 key 的唯一性生成 map 对象来获取对应节点，比遍历方式更快

**如何选取key值？**

我们在使用key时，应该尽量保证key是不会变化的，只有记住这个原则，我们才能享用虚拟DOM以及Diffing算法所带来的优越性，否则性能只会越来越差

**index：**

使用index作为key：如果不存在对数据的逆序添加、逆序删除等破坏顺序的操作，仅渲染列表用于展示，使用index作为key是没有问题的

**唯一值：**

使用唯一的值作为key：最好将每条数据的唯一标识用作key，比如id、学号等唯一值；如果确定只是简单的展示数据，使用index也是可以的

### 6.为什么不建议用index作为key？

使用index 作为 key和没写基本上没区别，因为不管数组的顺序怎么颠倒，index 都是 0, 1, 2...这样排列，导致 Vue 会复用错误的旧子节点，做很多额外的工作。

## 三、VUE生命周期相关

### 1.什么是 vue 生命周期？有什么作用？

答：Vue 实例有一个完整的生命周期，也就是从开始创建、初始化数据、编译模版、挂载 Dom -> 渲染、更新 -> 渲染、卸载等一系列过程，我们称这是 Vue 的生命周期。

每个 Vue 实例在被创建时都要经过一系列的初始化过程——例如，需要设置数据监听、编译模板、将实例挂载到 DOM 并在数据变化时更新 DOM 等。同时在这个过程中也会运行一些叫做生命周期钩子的函数，这给了用户在不同阶段添加自己的代码的机会。（ps：生命周期钩子就是生命周期函数）例如，如果要通过某些插件操作DOM节点，如想在页面渲染完后弹出广告窗， 那我们最早可在mounted 中进行。

<img src="F:\面试相关\面试题总结\图片\VUE生命周期.png" alt="VUE生命周期" style="zoom:200%;" />

### 2. Vue的生命周期方法有哪些？一般在哪一步发送请求？

| 生命周期      | 描述                                                         |
| ------------- | ------------------------------------------------------------ |
| beforeCreate  | 组件实例被创建之初，组件的属性生效之前，data和methods中的数据都没有被初始化 |
| created       | 实例创建完成，实例上配置的 options 包括 data、computed、watch、methods 等都配置完成，但是此时渲染得节点还未挂载到 DOM，所以不能访问到 $el 属性。 |
| beforeMount   | 表示Vue开始编辑模板，将template模板字符串解析为AST，再根据AST动态生成渲染函数，相关render函数首次被调用。在内存中生成一个编译好的字符串，并没有真正挂载到真正的界面中 |
| mounted       | el 被新创建的 vm.$el 替换，并挂载到实例上去之后调用该钩子，此时**可以操作DOM元素** |
| beforeUpdate  | data是新的，DOM是旧的。随后进行虚拟DOM的patch过程，精细化更新 |
| update        | data是新的，DOM也是新的                                      |
| activited     | keep-alive 专属，组件被激活时调用。                          |
| deactivated   | keep-alive 专属，组件被销毁时调用。用 keep-alive 包裹的组件在切换时不会进行销毁，而是缓存到内存中并执行 deactivated 钩子函数，命中缓存渲染后会执行 activated 钩子函数。 |
| beforeDestory | 组件销毁前调用                                               |
| destoryed     | 组件销毁后调用                                               |

### 3. created和mounted的区别

- created方法在模板渲染成html前调用，通常用于初始化data中的某些属性值或者初始化methods中的一些方法
- mounted在模板渲染成html后调用，通常是初始化html页面后，再对页面中的一些dom进行一些需要的操作,此过程进行ajax交互

### **4.** 在哪个生命周期内调用异步请求？

答：可以在钩子函数 created、before-Mount、mounted 中进行调用，因为在这三个钩子函数中，data 已经创建，可以将服务端端返回的数据进行赋值。一般放在created中，此时数据刚被生成。但是涉及到需要页面加载完成之后的DOM操作可以将异步操作放在mounted中。

但是推荐在 created 钩子函数中调用异步请求，因为在 created 钩子函数中调用异步请求有以下优点：

- 能更快获取到服务端数据，减少页面 loading 时间；
- ssr 不支持 beforeMount 、mounted 钩子函数，所以放在 created 中有助于一致性；

### 5.第一次页面加载会触发哪几个钩子？

答：beforeCreate， created， beforeMount， mounted

### 6.请详细说下你对vue生命周期的理解？

答：总共分为8个阶段创建前/后，载入前/后，更新前/后，销毁前/后。

**BeforeCreate/created**： 在beforeCreated阶段，vue实例的挂载元素$el、methods、 data都为undefined，还未初始化。在**created**阶段，vue实例的数据对象data有了，$el还没有。

**beforeMount/mounted**：在**beforeMount**阶段，模板已经编译完成，在内存中，尚未把模板渲染到页面中。而且在beforeMount执行时，页面中的元素尚未被真正替换，只是之前写的一些模板字符串（vue实例的$el和data都初始化了，但还是挂载之前为虚拟的dom节点，data.message还未替换）。在**mounted**阶段，vue实例挂载完成，data.message成功渲染,表示内存中的模板，已经真实的挂载到了页面中，用户已经可以看到渲染号的页面了。是实例创建期间的最后一个生命周期函数，当执行完mounted就表示实例已经被完全创建好了，组件已经脱离了创建阶段，进入了运行阶段。此时如果没有其他操作，实例就静静的存储在内存中。如果要通过某些插件操作页面上的DOM节点，最早要在mounted中进行

**beforeUpdate /Update**：当data变化时，会有选择性的触发beforeUpdate和updated方法。

BeforeUpdate表示界面还没被更新，但数据已经被更新了。此步表示先根据data中的最新数据，在内存中重新渲染一份最新的内存DOM树，并将其重新渲染到真实的页面当中去，完成了从data（Model层）-> view（视图层的更新）。即Update事件执行时，页面和数据已经保持同步了，都是最新的

beforeDestory/destoryed：在beforeDestory时，实例上所有的data和所有methods等都处于可用状态，还未真正执行销毁

在执行destroy方法后，对data的改变不会再触发周期函数，说明此时vue实例已经解除了事件监听以及和dom的绑定，但是dom结构依然存在。

### 8. Vue 的父组件和子组件生命周期钩子函数执行顺序？

加载渲染过程：
1. 父组件 beforeCreate
2. 父组件 created                 //拿到data和methods
3. 父组件 beforeMount        //此时还未正式渲染DOM，需要联合子组件一同渲染，所以不继续created生命周期
4. 子组件 beforeCreate      
5. 子组件 created
6. 子组件 beforeMount       
7. 子组件 mounted              //成功渲染子组件的DOM内容
8. 父组件 mounted           	//渲染父组件的DOM内容

1. 父组件 beforeUpdate
2. 子组件 beforeUpdate
3. 子组件 updated
4. 父组件 updated

销毁过程：

1. 父组件 beforeDestroy
2. 子组件 beforeDestroy
3. 子组件 destroyed
4. 父组件 destoryed

### 9. 父组件可以监听到子组件的生命周期吗？

#### 1.使用`$emit`

比如有父组件 Parent 和子组件 Child，如果父组件监听到子组件挂载 mounted 就做一些逻辑处理，可以通过`$emit`实现

```js
// 父组件
<template>
  <div>
    <Child
      @mounted="onMounted"
      @updated="onUpdated"
      @beforeDestroy="onBeforeDestroy"
    ></Child>
  </div>
</template>

// 子组件
...
  mounted () {
	  this.$emit('mounted')
  }

  updated () {
	  this.$emit('updated')
  }
  beforeDestroy () {
	  this.$emit('beforeDestroy')
  }
...

```

#### 2.@hooks

以上需要手动通过 $emit 触发父组件的事件，更简单的方式可以在父组件引用子组件时通过 @hook 来监听即可，如下所示：

```html
// 父组件
<template>
  <div>
    <Child
      @hook:mounted="onMounted"
      @hook:updated="onUpdated"
      @hook:beforeDestroy="onBeforeDestroy"
    ></Child>
  </div>
</template>

// 子组件
<!--无-->   //子组件无需相关代码就能触发父组件通过@hook:绑定的事件，

```

在`lifecycle.js`文件里，我们发现`vue`的生命周期的各个阶段都会去调用一个`callHook`函数，它支持两个参入，分别是实例`vm`和对应的生命周期钩子名称。而`callHook`里面就执行了`vm.$emit('hook:' + hook)`，看到这里，大家应该就有点熟悉了，这不就是刚才的方法一吗！所以方法二巧妙的地方就是复用了vue自身的逻辑。当我们在子组件上传入了对应的`@hook:mounted`钩子，也就是执行了`vm.$on('hook:mounted')`，而vue实例在生命周期里本身就会执行`vm.$emit('hook:mounted')`,其实就连带着触发了我们绑定给子组件的回调函数了。

当然 @hook 方法不仅仅是可以监听 mounted，其它的生命周期事件，例如：created，updated 等都可以监听。

### 10. keep-alive 中的生命周期哪些

- keep-alive是 Vue 提供的一个内置组件，用来对组件进行缓存——在组件切换过程中将状态保留在内存中，防止重复渲染DOM。
- 如果为一个组件包裹了 keep-alive，那么它会多出两个生命周期：deactivated、activated。同时，beforeDestroy 和 destroyed 就不会再被触发了，因为组件不会被真正销毁。
- 当组件被换掉时，会被缓存到内存中、触发 deactivated 生命周期；当组件被切回来时，再去缓存里找这个组件、触发 activated钩子函数。



## 四、VUE指令相关

### 0. 写过自定义指令吗？原理是什么？

#### **1.使用场景**

在 Vue2.0 中，代码复用和抽象的主要形式是组件。然而，有的情况下，你仍然需要对普通 DOM 元素进行底层操作，这时候就会用到自定义指令。自定义指令是用来操作DOM的。尽管Vue推崇数据驱动视图的理念，但并非所有情况都适合数据驱动。自定义指令就是一种有效的补充和扩展，不仅可用于定义任何的DOM操作，并且是可复用的。（指令本质上是装饰器，是 vue 对 HTML 元素的扩展，给 HTML 元素添加自定义功能。vue 编译 DOM 时，会找到指令对象，执行指令的相关方法。

自定义指令有五个生命周期（也叫钩子函数），分别是 bind、inserted、update、component-Updated、unbind）

>bind： 指令第一次绑定到元素时调用，在这里可以进行一次初始化设置
>
>inserted：被绑定的节点插入到父节点中时调用（仅保证父节点存在，但不一定已经被插入到文档中）
>
>update：所在组件的VNode更新时调用，简单来说是页面上有dom元素发生改变的时候，执行改钩子函数。（组件更新前调用）
>
>componentUpdated：指令所在组件的VNode及其子VNode全部更新后调用（组件更新后调用）
>
>unbind：指令与元素解绑后调用

#### **2.使用方法**

例：在做数据大屏或自适应开发时，根据浏览器窗口大小变化重新渲染页面。resize指令在窗口大小发生变化时，实时打印最新的窗口宽高

```js
//首先在main.js中使用directive设置全局自定义组件
//在全局中设置自定义指令
Vue.directive("resize",{    //指令的名称，指令的生命周期函数(钩子函数),一次只能设置一个
    bind(){},            //vue2的写法，vue3中变更为mounted
    inserted(){},
    update(){},
    componentUpdated(){},
    unbind(){},

})

//局部设置自定义指令，使用directives方法，与methods，components和data同级.directives中可以定义很多自定义指令，所以加’s'
data(){
    return {
        args:'this is arguements',
        value:'arguement value'
    }
}
directives:{
    resizes:{ //钩子函数中不能调用this，this被代替为vnode，表示当前的操作节点
        bind(el,binding，vnode){   //el:指令绑定的dom节点，可以直接操作DOM； binding:一个对象，自带一些属性
            console.log(binding.value)
            console.log(binding.arg)
        },
        inserted(){},
        update(){},
        componentUpdated(){},
        unbind(){},
    }
}

//使用
<div v-resizes:[args] = "value" ></div>   //如果不使用括号[]，则传递的是字符串args。而value是一种表达式或者变量，如果data中没有value，则会报错，undefined。这也说明想要传递字符串，需要使用专门的语法expression

```

#### 3.自定义指令在VUE2.0和VUE3.0中的使用区别

- VUE2中原本的inserted没了，很多函数也没了，取而代之的是mounted, beforeMounted,updated,beforeUpdated, beforeUnmount等，使用的时候要注意到这些。
- vue3不建议操作参数vnode，而是操作el，因为vnode包含很多额外的函数、属性，修改容易发生错误。
- binding中的新旧值就是value和oldValue，不再有什么arg

#### 4.常用的自定义指令

v-copy：实现一键复制文本内容

v-longpress: 鼠标长按触发相应事件

v-debounce: 防止按钮在短时间内被多次点击，实现**防抖**，配合js中的防抖函数

v-lazyLoad: 实现图片懒加载，只加载可见区域的图片

v-draggable: 可以在页面可视区域任意拖拽元素

初级应用：
●鼠标聚焦
●下拉菜单
●相对时间转换
●滚动动画
高级应用：
●自定义指令实现图片懒加载
●自定义指令集成第三方插件

### **1.**说出几种vue当中的指令和它的用法？

- v-bind：**单向绑定**解析表达式，动态更新HTML元素上的属性。例如 v-bind:class。`:to={ XXXX }`则是把括号内的内容当成语法解析，而不是对象数据。语法糖 `：`

- v-model： 双向数据绑定

- v-for : 遍历数组/对象/字符串

- v-on ：绑定**事件监听**，.可简写为`@`

- v-if :  条件渲染(动态控制节点是否存存在)

- v-else：条件渲染(动态控制节点是否存存在)

- V- show：条件渲染(动态控制节点是否展示)

- v-once - 定义它的元素或组件只渲染一次，包括元素或组件的所有节点，首次渲染后，不再随数据的变化重新渲染，将被视为静态内容。 

- v-cloak - 这个指令保持在元素上直到关联实例结束编译 -- 解决当网速较慢，加载页面时，可能会出现未经渲染的{{msg}}, 可以配合css解决。

  >第一步：在css中给定义属性选择器          [v-cloak]{  display:none }
  >
  >第二步：在对应标签中加入 v-cloak:         例如：<div id="wrap"  v-cloak></div>
  >
  >此方案的运行机制： vue实例创建完成后会把v-cloak去掉，在没创建实例对象时，该标签内的内容都会被隐藏

- v-text - 更新元素的textContent，向其所在的节点中渲染文本内容。
  2.与插值语法的区别: v-text会 替换掉节点中的内容，{{xx}}则不会

- v-html - `v-html`是内容渲染指令，用来辅助开发者渲染- DOM 元素的文本内容,设置或更新元素的内容 --但是在网站上动态渲染HTML是非常危险的，容易导致XSS攻击，只可在信任内容上使用v-html，永不在用户提交内容上

> `v-text`会将内容原样输出，而`v-html`会对内容**进行html解析**，如果内容是合法的html结构，则会解析出对应的网页结构

> innerHTML在JS是双向功能：获取对象的内容  或  向对象插入内容；
> 如：<div id="aa">这是内容</div> ，
> 我们可以通过  document.getElementById('aa').innerHTML 来获取id为aa的对象的内嵌内容；
> 也可以对某对象插入内容，如  document.getElementById('abc').innerHTML='这是被插入的内容';   
> 这样就能向id为abc的对象插入内容。

- v-pre - 跳过这个元素以及子元素的编译过程，以此来加快整个项目的编译速度。

### 2.v-show和v-if指令的共同点和不同点？

**共同点**：都能控制元素的显示和隐藏；

**不同点：**

v-if 是真正的条件渲染，因为它会确保在切换过程中条件块内的事件监听器和子组件适当地被销毁和重建；也是惰性的：如果在初始渲染时条件为假，则什么也不做——直到条件第一次变为真时，才会开始渲染条件块；v-show 就简单得多——不管初始条件是什么，元素总是会被渲染，并且只是简单地基于 CSS 的 “display” 属性进行切换。

- 手段：v-if是动态的向DOM树内添加或者删除DOM元素；v-show是通过设置DOM元素的display样式属性控制显隐；
- 编译过程：v-if切换有一个局部编译/卸载的过程，切换过程中合适地销毁和重建内部的事件监听和子组件；v-show只是简单的基于css切换；
- 编译条件：v-if是惰性的，如果初始条件为假，则什么也不做；只有在条件第一次变为真时才开始局部编译; v-show是在任何条件下，无论首次条件是否为真，都被编译，然后被缓存，而且DOM元素保留；
- 性能消耗：v-if有更高的切换消耗；v-show有更高的初始渲染消耗；
- 使用场景：v-if适合运营条件不大可能改变；v-show适合频繁切换。v-if 适用于在运行时很少改变条件，不需要频繁切换条件的场景；v-show 则适用于需要非常频繁切换条件的场景。

### 3. v-if、v-show、v-html 的原理

- v-if会调用`addIfCondition`方法，生成`vnode`的时候会忽略对应节点，`render`的时候就不会渲染, 即动态的向DOM树内添加或者删除DOM元素
-  v-show会生成`vnode`，`render`的时候也会渲染成真实节点，只是在render过程中会在节点的属性中修改show属性值，也就是常说的display； 
- v-html与v-text区别在于v-text输出的是纯文本，浏览器不会对其再进行html解析，但v-html会将其当html标签解析后输出。他会先移除节点下的所有节点，调用html方法，通过addProp添加innerHTML属性，归根结底还是设置innerHTML为v-html的值。也可以使用{{{vm.data}}}三个大括号来包裹对象，解析数据中存在的html标签，但是会出现bug。

### 4.如何理解slot？Slot在什么场景下用？

**目的**：让封装的组件更加具有扩展性，让使用者决定组件内部的一些内容到底展示什么。·**封装共性，插槽中为不同内容**。简单来说，假如父组件需要在子组件内放一些DOM，那么这些DOM是显示、不显示、在哪个地方显示、如何显示，就是slot分发负责的活。（slot可以设定默认值）

**原理：**当子组件vm实例化时，获取到父组件传入的slot标签的内容，存放在`vm.$slot`中，默认插槽为`vm.$slot.default`，具名插槽为`vm.$slot.xxx`，xxx 为插槽名，当组件执行渲染函数时候，遇到slot标签，使用`$slot`中的内容进行替换，此时可以为插槽传递数据，若存在数据，则可称该插槽为作用域插槽。

**具名插槽**：替换有name属性的slot时，必须使用slot=“name”属性指定，与之对应的，无name则称为**匿名插槽**

**作用域插槽**：在插槽上绑定数据（父组件替换插槽的标签，但内容由子组件提供）

Ps：父组件模板的所有东西都会在父级作用域内编译，子组件模板的所有东西都会在子级作用域内编译

**使用场景**： 移动网站中的导航栏

- 移动开发中，几乎每个页面都有导航栏，必然会封装成一个插件/组件，这样就可以在多个页面复用这个导航组件。**但是每页的导航组件内容是不同的，可以使用slot封装这类组件**
- 这表示slot封装的组件有很多共性，也有很多区别。所以我们抽取共性，将不一样的内容预留为插槽

```html
<div>
    <cpn></cpn>                                //显示slot0，默认值
	<cpn><button>slot1</button> </cpn>        //显示哈哈哈，slot1
	<cpn> <button>slot2</button> </cpn>        //显示哈哈哈，slot2
    <cpn> <span slot='testname'></span> </cpn>   //替换具名插槽中的内容,显示this slot have a name
    <cnp> 
        <span v-for= "item in slot.data">{{ item }} </span>      //此时data是testdata，使用作用域插槽传递数据  
    </cnp>
    
</div>


<template id='cpn'>
	<div>
		<h1>哈哈哈哈</h1>
		<slot>    //匿名插槽
			<button>slot0</button>
		</slot>
        <slot name='testname'>
            <span>this slot have a name</span>
        </slot>   //具名插槽
        <slot :data='testdata' ></slot>    //作用域插槽，绑定数据
	</div>
</remplate>
```

### 5. v-if和v-for的优先级

**VUE2.0中，当 v-if 与 v-for 一起使用时，v-for 具有比 v-if 更高的优先级**，这意味着 v-if 将分别重复运行于每个 v-for 循环中。

源码分析：编译有三个过程，`parse`->`optimize`->`generator`。在`generator`生成render字符串时，会先解析`AST`树中的与`v-for`相关的属性，再解析与`v-if`相关的属性

当同时使用时，可以使用`app.$option.render`查看渲染函数

```js
ƒ anonymous() {
  with (this) { return 
    _c('div', { attrs: { "id": "app" } }, 
    _l((list), function (item)              //v-for指令
    { return (isShow) ? _c('p', [_v("\n" + _s(item.name) + "\n")]) : _e() }), 0) }   //v-if判断
}
 //可以看到同时使用两个指令时，v-for的每次循环中都包括了v-if的条件判断，所以v-for的优先级高于v-if
```

>**VUE3.0 中，v-if的优先级高于v-for**

v-for优先于v-if被解析，如果同时出现，每次渲染都会先执行循环再判断条件，无论如何循环都不可避免，浪费了性能。要避免出现这种情况，则在外层嵌套template，在这一层进行v-if判断，然后在内部进行v-for循环。如果条件出现在循环内部，可**通过computed计算属性提前过滤**掉那些不需要显示的项。

```html
//不推荐使用
<ul>
    <li v-for='user in users' v-if = 'shouldShowUser' :key = 'usre.id'> {{ user.name }} </li>
</ul>

//推荐使用,把v-if放在外层
<ul v-if = 'shouldShowUser'>
    <li v-for='user in users' :key = 'usre.id'> {{ user.name }} </li>
</ul>
//或者在外层使用template，将v-if包裹
<template v-if = "isShow">
	<p v-for = "{ item in items }"></p>  
</template>
```

### 6. vue-loader是什么？使用它的用途有哪些？

**定义：**Vue-loader是一个webpack加载器，解析和转换VUE组件，提取出其中的逻辑代码 script,样式代码style,以及HTML 模板template，分别把他们交给对应的loader处理。他**可以把一个标准的VUE组件转化为js模块。**最值得关注的是，它生成了`render function code`, 我们可以通过改造 Vue-loader 来改写 `render function code` 的生成结果，从而全局的影响组件的每一次渲染结果

> `render function code` 是从模板编译而来（可以并且应该预编译）的组件核心渲染方法，在每一次组件的 Render 过程中，通过注入的数据执行可生成虚拟 Dom

  **用途：**

- template
  1.默认语言 HTML
  2.每个.vue文件最多包含一个
  3.内容被提取为成字符串，可以加jade(简化代码的书写方式)

- script
  1.默认语言 JS
  2.每个文件最多包含一个
  3.可以写es6
- style
  1.默认语言 css
  2.一个vue文件可以包含多个style标签
  3.可以写scss和less,还能用stylus写样式      

### 7.v-on可以监听多个方法吗？

可以，栗子：

```html
<input type="text" v-on="{ input:onInput,focus:onFocus,blur:onBlur, }">  //blur是一个css滤镜，表示模糊效果
```

### 8. v-model的原理和实际的语法糖

说到v-model，就想到了双向数据绑定，而且往往最常见的是在表单元素`<input>,<textarea>,<select>`中的使用，在一些自定义组件中也使用到了v-model。v-model 本质上不过是语法糖，v-model 在内部为不同的输入元素使用不同的属性并抛出不同的事件：

>v-model 在内部为不同的输入元素使用不同的属性并抛出不同的事件。默认情况下，一个组件上的v-model会把value用作prop且把input用作event。**但是一些输入类型比如单选框和复选框按钮可能想使用 value prop 来达到不同的目的。**所以可以使用model方法自行设置prop和event的对象（model与data/methods 同级）.
>text 和 textarea 元素使用 value 属性和 input 事件；
>checkbox 和 radio 使用 checked 属性和 change 事件；
>select 字段将 value 作为 prop 并将 change 作为事件。

以 input 表单元素为例，使用 **v-bind:绑定响应式数据，触发 input 事件并传递数据 (核心和重点)**

```html
data(){
	return {
		message:""
	}
}

<input v-model="message" />
//等同于
<input :value="message" @:input="message=$event.target.value" >


//$event 指代当前触发的事件对象;
//$event.target 指代当前触发的事件对象的dom;
//$event.target.value 就是当前dom的value值;
//在@input方法中，value => sth;
//在:value中,sth => value;
```

#### Vue自定义组件使用v-model

Vue允许自定义组件在使用v-model时定制prop和event,即根据需求，自定义v-model双向绑定的响应事件。默认情况下，一个组件上的v-model会把value用作prop且把input用作event，但是一些不同的输入框可能不想默认使用value和input，使用model属性可以避免这些情况产生的冲突

```js
//--------------父组件中-----------------------------------
<template>
  <div>
     <h3>parent: {{ msg1 }}</h3>
     <son1 v-model="msg1"></son1>
<!--     等同于: :value="msg1"  @input="msg1 = $event "-->  //按照这个原型，进行父子组件的相互通信
      <br>
      <h3>parent : {{msg2}}</h3>
      <son2 v-model="msg2"></son2>
<!--      等同于 :checked="msg2" @change="msg2 = $event"-->   //按照原型，进行父子组件之间的相互通信
    //这更表明了v-model是一个已经封装好的语法糖


  </div>
</template>

<script>
    import son1 from "@/components/son1";
    import son2 from "@/components/son2";
    export default {
        name: "parent",
        components:{
            son1,
            son2
        },
        data(){
            return{
               msg1:'this is msg1',
               msg2:true
            }
        },
        methods:{

        }
    }
</script>

<style scoped>

</style>


//------------------------------------son1组件中--------------------------------------
<template>
    <div>
        <input type="search" :value="value" @input="sonInput">
        <h3> son1:{{ value }} </h3>

    </div>
</template>

<script>
    export default {
        name: "son1",
        props:{
            "value":[String,Number]
        },
        data(){
            return{

            }
        },
        methods:{
            sonInput(e){
                this.$emit('input', e.target.value)
            }
        }
    }
</script>

<style scoped>

</style>

//------------------------------------son2组件中--------------------------------------
<template>
    <div>
        <input type="checkbox" :checked = "checked"  @change="setCheck">
        <br>

    </div>
</template>

<script>
    export default {
        name: "son2",
        data(){
            return{

            }
        },
        model:{
            props: 'checked',
            event:'change'
        },
        props:{
            "checked":Boolean
        },
        methods:{
             setCheck(e){
                 this.$emit('change',e.target.checked)
            }
        },
    }
</script>

<style scoped>

</style>
```

### 9.sync修饰符的理解

v-model 只能绑定一个属性（在一个组件或元素上，v-model 只能写一次，当然如果是具名的（VUE3），则可以有多个，比如 v-model:a v-model:b 等等），如果父组件有多个需要和子组件的做双向绑定的属性怎么办？你可以会想到用对象或者数组。但是这可以会导致操作过于复杂。然而可以用 `.sync` 修饰符完成。**.sync修饰符可以实现子组件与父组件的双向绑定，并且可以实现子组件同步修改父组件的值。**使用方法如下：

```js
// 正常父传子： 
<son :a="num" :b="num2"></son>

// 加上sync之后父传子： 
<son :a.sync="num" .b.sync="num2"></son> 

// 它等价于
<son
  :a="num" @update:a="val=>num=val"
  :b="num2" @update:b="val=>num2=val"></son> 

// 相当于多了一个事件监听，事件名是update:a，回调函数中，会把接收到的值赋值给属性绑定的数据项中。

```

##### 1.sync与v-model区别是

**相同点**：都是语法糖，都可以实现父子组件中的数据的双向通信。

**区别点**：格式不同：

```js
v-model=“num”, :num.sync=“num”   //使用方法

v-model： @input + value        //v-model一般绑定的是input和value事件
:num.sync: @update:num          //sync在向父组件回传值时$emit所调用的事件名必须是update:属性名
```

**另外需要特别注意的是:**  **`v-model`只能用一次；`.sync`可以有多个。**

### 10. Class 与 Style 如何动态绑定？

#### 1.对象语法

Class 和style可以通过对象语法进行动态绑定，对象语法以帮助元素动态的切换class

```html
<div class="test" v-bind:class="{ active: isActive, 'text-danger': hasError }"></div>
<div v-bind:style="{ color: activeColor, fontSize: fontSize + 'px' }"></div>
<div :class="[isActive ? activeClass : '', errorClass]"></div>   //errorClass:条件不满足 ，三元表达式动态切换class，推荐方法

data:{
	isActive:true,
	hasError:false
}

//渲染结果
<div class = "test active "></div>
```

#### 2.数组语法

数组语法，可以把一个数组传给 v-bind:class，以应用一个 class 列表：例：

```html
<div v-bind:class="[activeClass, errorClass]"></div>
<div v-bind:style="[styleColor, styleSize]"></div>

data: {
  activeClass: 'active',
  errorClass: 'text-danger'
}
渲染为：
<div class="active text-danger"></div>

```

#### 3.计算属性

```js
<div :class="classObject"></div>
data: {
  isActive: true,
  error: null
},
computed: {
  classObject: function () {
    return {
      active: this.isActive && !this.error,	//isActive为true，且error不为null
      text-danger: this.error && this.error.type === 'fatal'
        //error为null且this.error.type === 'fatal'
    }
  }
}
```

### 11. delete和Vue.delete删除数组的区别

delete：普通的delete删除一个数组中的元素，该元素会成为空值，其他的元素的键值还是不变，数组长度也不变。

Vue.delete ：直接删除了数组中的一个元素，数组长度会减少

### 12. 分别简述computed和watch的区别和使用场景

#### 1.为什么说computed是有缓存值的?

`computed` 会拥有自己的 `watcher`，它内部有个属性 `dirty` 开关来决定 `computed` 的值是需要重新计算还是直接复用之前的值。「dirty」 从字面意义来讲就是 `脏` 的意思，这个开关开启了，就意味着这个数据是脏数据，需要重新求值了拿到最新值。

```js
computed: {
    sum() {
        return this.count + 1
    }
}
```

**理解思路：**

- 在 `sum` 第一次进行求值的时候会读取响应式属性 `count`，收集到这个响应式数据作为依赖。并且计算出一个值来保存在自身的 `value` 上，把 `dirty` 设为 false，接下来在模板里再访问 `sum` 就直接返回这个求好的值 `value`，并不进行重新的求值，直接调用get方法
- 而 `count` 发生变化了以后会通知 `sum` 所对应的 `watcher` 把自身的 `dirty` 属性设置成 true，这也就相当于把重新求值的开关打开来了。这个很好理解，只有 `count` 变化了， `sum` 才需要重新去求值。
- 那么下次模板中再访问到 `this.sum` 的时候，才会真正的去重新调用 `sum` 函数求值（调用get方法），并且再次把 `dirty` 设置为 false，等待下次的开启……

#### 2.Watch中的deep:true是如何实现的？

```js
//watch的使用
import { watch } from 'vue'

//单项监听
setup(props){
         const state = reactive({ 
           count: 0 ,
           message:'Hellow world'
         });
         watch(state,()=>{
            console.log(state.count); --单个监听
         })
         return {
           state,
         }
},

//多项监听
 watch([obj, obj1], () => {
     console.log(obj.name)
     if(obj.age>28){
         watchFunc()  // 停止监听`
     }
   }, {
     // 页面加载会先执行一次
     immediate: true
   })

//监听数组
const arrayRef = ref([1, 2, 3, 4])
const arrayReactive = reactive([1, 2, 3, 4])
//ref deep
const arrayRefDeepWatch = watch(arrayRef, (newValue, oldValue) => {
      console.log('newArrayRefDeepWatch', newValue, 'oldArrayRefDeepWatch', oldValue)
 }, {deep: true})

// 数组监听的最佳实践- reactive且源采用函数式返回，返回拷贝后的数据
const arrayReactiveFuncWatch = watch(() => [...arrayReactive], (newValue, oldValue) => {
      console.log('newArrayReactiveFuncWatch', newValue, 'oldArrayReactiveFuncWatch', oldValue)
})

//监听对象
const objReactive = reactive({user: {name: '小松菜奈', age: '20'}, brand: 'Channel'})
const objReactiveDeepWatch = watch(() => objReactive, (newValue, oldValue) => {
        console.log('objReactiveDeepWatch')
        console.log('new:',JSON.stringify(newValue))
        console.log('old:',JSON.stringify(oldValue))
      }, {deep: true})
```

- 如果当前监控的值是数组类型，会对对象中的每一项进行求值，此时会将当前watcher存入到对应属性的依赖中，这样数组中的对象发生变化时也会通知数据更新。
- 当监控的值是obj时，那么对 `obj.a.b.c = 5` 这样深层次的修改也一样会触发 watch 的回调函数。本质上是因为 Vue 内部对需要 `deep watch` 的属性会进行**`递归的访问`**，而在此过程中也会不断发生依赖收集。（只要此属性也是`响应式属性`）

**对于computed：**

● 它支持缓存，只有依赖的数据发生了变化，才会重新计算
● 不支持异步，当Computed中有异步操作时，无法监听数据的变化
● computed的值会默认走缓存，计算属性是基于它们的响应式依赖进行缓存的，也就是基于data声明过，或者父组件传递过来的props中的数据进行计算的。
● 如果一个属性是由其他属性计算而来的，这个属性依赖其他的属性，一般会使用computed
● 如果computed属性的属性值是函数，那么默认使用get方法，函数的返回值就是属性的属性值；在computed中，属性有一个get方法和一个set方法，当数据发生变化时，会调用set方法。

**对于Watch：**
● 它不支持缓存，数据变化时，它就会触发相应的操作
● 支持异步监听
● 监听的函数接收两个参数，第一个参数是最新的值，第二个是变化之前的值
● 当一个属性发生变化时，就需要执行相应的操作
● 监听数据必须是data中声明的或者父组件传递过来的props中的数据，当发生变化时，会触发其他操作，函数有两个的参数：

- immediate：组件加载立即触发回调函数
- deep：深度监听，发现数据内部的变化，在复杂数据类型中使用，例如数组中的对象发生变化。需要注意的是，deep无法监听到数组和对象内部的变化。
  当想要执行异步或者昂贵的操作以响应不断的变化时，就需要使用watch。

<img src="C:\Users\SFONE\AppData\Roaming\Typora\typora-user-images\image-20220627160506690.png" alt="image-20220627160506690" style="zoom: 67%;" />

**总结：**
● computed 计算属性 : 依赖其它属性值，并且 computed 的值**有缓存**，只有它依赖的属性值发生改变，下一次获取 computed 的值时才会重新计算 computed 的值。 购物车结算
● watch 侦听器 : 更多的是**观察**的作用，**无缓存性**，类似于某些数据的监听回调，每当监听的数据变化时都会执行回调进行后续操作。 

**运用场景：** 
● 当需要进行**数值计算,并且依赖于其它数据时**，应该使用 computed，因为可以利用 computed 的缓存特性，避免每次获取值时都要重新计算。 
● 当需要在数据变化时执行异步或开销较大的操作时，应该使用 watch，使用 watch 选项允许执行异步操作 ( 访问一个 API )，限制执行该操作的频率，并在得到最终结果前，设置中间状态。这些都是计算属性无法做到的。 

### 13. Computed，watcher、methods的区别

可以将同一函数定义为一个 method 或者一个计算属性。对于最终的结果，两种方式是相同的 

不同点： 

- computed: 计算属性是基于它们的依赖进行缓存的，只有在它的相关依赖发生改变时才会重新求值；
- methods·里面定义的函数，是需要`主动调用`的，而和`watch`和`computed`相关的函数，会`自动调用`,完成我们希望完成的作用。
- methods里面定义的是函数，你显然需要像"fuc()"这样去调用它（假设函数为fuc）；computed是计算属性，事实上和和data对象里的数据属性是同一类的（使用上）；watch:类似于监听机制+事件机制
- 相比于watch/computed，**methods不处理数据逻辑关系，只提供可调用的函数**
- `methods`里面的函数就是一群“耿直Boy”，如果有其他父函数调用它，它会每一次都“乖乖”地执行并返回结果，即使这些结果很可能是相同的，是不需要的。而`computed`是一个“心机Boy”，它会以Vue提供的依赖追踪系统为基础，只要依赖数据没有发生变化,computed就不会再度进行计算


### 14. keep-alive的原理和使用方式

**1.定义**

缓存不活动的组件状态，避免多次重复渲染降低性能，一般结合router，缓存部分页面（$route.meta.kaapAlive）。如果需要在组件切换的时候，保存一些组件的状态防止多次渲染，就可以使用 keep-alive 组件包裹需要保存的组件。keep-alive不会生成真正的DOM节点。有以下三个属性：

- include 字符串或正则表达式，只有名称匹配的组件会被匹配；
- exclude 字符串或正则表达式，任何名称匹配的组件都不会被缓存；
- max 数字，最多可以缓存多少组件实例。

注意：keep-alive 包裹动态组件时，会缓存不活动的组件实例。并且keep-alive是一个抽象组件，本身不会渲染DOM元素，也不会出现在组件的父组件链中

**2.使用场景**

如果未使用keep-alive组件，在路由切换会对界面进行销毁，在某些业务场景下会使用户体验不是很友好。

- 主页面跳转详情页再次从详情页跳转回主页面的时候需要主页面保留搜索条件以及数据。（持久化页面）
- 后台系统常见的跳转后添加顶部标签，标签之间切换期望保留数据。

**3.缺点：**

- 不能保证系统的数据时效性。
- keep-alive 的本质是保持页面不销毁，这样会增加内存的占用。

**4.生命周期**

当组件在keep-alive中被切换时，它的activated和deactivated两个生命周期钩子函数会被执行。

- 初次进入时：created > mounted > activated；退出后触发 deactivated
- 再次进入：会触发 activated；事件挂载的方法等，只执行一次的放在 mounted 中；组件每次进去执行的方法放在 activated 中

**5.使用方式**

```html
//在router.js中，设置组件是否被缓存
{
	name:'111',
	path:'/1111',
	meta:{
		keepAlive:true
	}
}

//使用
<keep-alive> 
	<router-view  v-if='$route.meta.keepAlive' />     //缓存使用这个路由
</keep-alive>

<keep-alive inclued ='a,b' exclude =[a,b] > </keep-alive>
	<router-view  v-if='!$route.meta.keepAlive' />    //不缓存使用另外的路由
```

**6.实现步骤：**

1. 接收数据，keep-alive中的props中有三个属性，include，exclude，max

2. created周期中会创建一个cache对象，用作缓存容器，保存vnode节点；相应的，destoryed周期会清除缓存容器

3. render钩子函数（核心）：遵循最近最少使用（LRU）

   1. 使用`getComponentChild`获得第一个子组件的name，和include，exclude匹配，如果匹配不成功，则表示不缓存该组件，直接返回
   2. 如果匹配成功，先判断this.cache中是否存在该对象，如果有，则将之前的删除，把name放在cache的末尾
   3. 如果没有缓存，则将其放入cache的末尾，并判断cache数组是否超出max，超出则删除第一个缓存组件
   4. 循环判断

4. mounted生命周期：如果include或exclude发生了变化，执行pruneCache函数。主要检查Cache中缓存的组件是否符合新的匹配规则，如果不匹配，则将其移除

```js
const patternTypes: Array<Function> = [String, RegExp, Array] // 接收：字符串，正则，数组

export default {
  name: 'keep-alive',
  abstract: true, // 抽象组件，是一个抽象组件：它自身不会渲染一个 DOM 元素，也不会出现在父组件链中。

  props: {
    include: patternTypes, // 匹配的组件，缓存
    exclude: patternTypes, // 不去匹配的组件，不缓存
    max: [String, Number], // 缓存组件的最大实例数量, 由于缓存的是组件实例（vnode），数量过多的时候，会占用过多的内存，可以用max指定上限
  },

  created() {
    // 用于初始化缓存虚拟DOM数组和vnode的key
    this.cache = Object.create(null)
    this.keys = []
  },

  destroyed() {
    // 销毁缓存cache的组件实例
    for (const key in this.cache) {
      pruneCacheEntry(this.cache, key, this.keys)
    }
  },

  mounted() {
    // prune 削减精简[v.]
    // 去监控include和exclude的改变，根据最新的include和exclude的内容，来实时削减缓存的组件的内容
    this.$watch('include', (val) => {
      pruneCache(this, (name) => matches(val, name))
    })
    this.$watch('exclude', (val) => {
      pruneCache(this, (name) => !matches(val, name))
    })
  },
}
```

### 15.如何理解ref指令？

虽然在 `Vue` 中不提倡我们直接操作 `DOM`，毕竟 `Vue` 的理念是以数据驱动视图。但是在实际情况中，我们有很多需求都是需要直接操作 `DOM` 节点的，这个时候 `Vue` 提供了一种方式让我们可以获取 `DOM` 节点：**ref 属性**。`ref` 属性是 `Vue2` 和 `Vue3` 中都有的，但是使用方式却不大一样


```js
//vue2使用ref
<template>
  <div id="app">
    <div ref="hello">小猪课堂</div>   //给DOM元素添加ref属性
  </div>
</template>
<script>
export default {
  mounted() {
    console.log(this.$refs.hello); // <div>小猪课堂</div>
  },
};
</script>

//vue3使用ref，在vue3中，没有this，想要获取ref，必须通过声明变量的方式
<template>
  <div ref="hello">小猪课堂</div>          //给DOM元素添加ref属性
</template>
<script setup lang="ts">
import { onMounted, ref } from "vue";
const hello = ref<any>(null);
onMounted(() => {
  console.log(hello.value); // <div>小猪课堂</div>
});
</script>

```

## 五、VUE数据传输相关

### 1. Vue 组件间通信有哪几种方式？

答：Vue 组件间通信是面试常考的知识点之一，这题有点类似于开放题，你回答出越多方法当然越加分，表明你对 Vue 掌握的越熟练。Vue 组件间通信只要指以下 3 类通信：A 和 B、B 和 C、B 和 D 都是**父子关系**，C 和 D 是**兄弟关系**，A 和 C 是**隔代关系**（可能隔多代）

![image-20220601163716856](C:\Users\SFONE\AppData\Roaming\Typora\typora-user-images\image-20220601163716856.png)

**总结**
**1.父子组件间通信**

- 子组件通过 props 属性来接受父组件的数据，然后父组件在子组件上注册监听事件，子组件通过 emit 触发事件来向父组件发送数据。

- 通过 ref 属性给子组件设置一个名字。父组件通过 $refs 组件名来获得子组件，子组件通过 $parent 获得父组件，这样也可以实现通信。

- 使用 provide/inject，在父组件中通过 provide提供变量，在子组件中通过 inject 来将变量注入到组件中。不论子组件有多深，只要调用了 inject 那么就可以注入 provide中的数据。

**2.兄弟组件间通信**

- 使用 eventBus 的方法，它的本质是通过创建一个空的 Vue 实例来作为消息传递的对象，通信的组件引入这个实例，通信的组件通过在这个实例上监听和触发事件，来实现消息的传递。

- 通过 $parent/$refs 来获取到兄弟组件，也可以进行通信。

**3.任意组件之间**

- 使用 eventBus ，其实就是创建一个事件中心，相当于中转站，可以用它来传递事件和接收事件。

#### 方法一 ：props（父传子）与emit（子传父）

父组件A通过props的方式向子组件B传递，使得父子组件之间形成了一个**单向下行绑定**。子组件的数据会随着父组件不断更新。

父组件将自己data中的数据绑定在自定义属性`msg`中，子组件在props中接收`msg`属性，并使用`{{msg}}`呈现变量中的数据

```js
// 父组件
<template>
    <div id="father">
        <son :msg="msgData" :fn="myFunction"></son>    //在调用子组件时，绑定props中的参数，msg和fn都是子组件props中的属性
    </div>
</template>

<script>
import son from "./son.vue";
export default {
    name: father,
    data() {
        msgData: "父组件数据";
    },
    methods: {
        myFunction() {
            console.log("vue");
        }
    },
    components: {
        son
    }
};
</script>
-----------------------------------------------------------------------------------------------------------------------------------------
//子组件
<template>
    <div id="son">
        <p>{{msg}}</p>
        <button @click="fn">按钮</button>
    </div>
</template>
<script>
export default {
    name: "son",
    props: ["msg", "fn"]
};
</script>
```

**2.子向父**通过 $emit 向父组件派发事件。在子组件中，使用$emit绑定一个自定义事件`listenToChildEvent`，并使用点击事件触发。父组件通过v-on监听并接收这个自定义事件`@子组件emit的事件 = 父组件中的响应事件`。父组件中的响应事件可以处理数据或者呈现数据。

```js
//子组件
<template>
    <div class="child">
        <h2>child子组件</h2>
        <!-- 第一步：绑定一个点击事件 -->
        <button @click="sendMsgToParent">点击向父组件传数据</button>
    </div>
</template>
<script>
export default {
    data() {
        return {
            message: '子组件的data'
        }
    },
    methods: {
        /** 
         * 第二步
        */
        sendMsgToParent() {
            //在子组件中使用$emit(eventName,data)来触发一个自定义事件，名叫eventName，并传递一个参数
            this.$emit('listenToChildEvent',this.message);
        }
    }
}
</script>

//父组件---------------------------------------------------------------------------------------------------------------------------------
<template>
    <div class="parent">
        <h1>子传父emit</h1>
        <hr>
       // 第三步 ：定义一个listenToChildEvent自定义事件监听子组件的emit触发，在父组件中的子标签中监听该自定义事件并添加一个响应该事件的处理方法 
            //将子组件中定义的事件传递给父组件自己的方法
        <child @listenToChildEvent='showMsgFromChild'></child>
        <p>来自于子组件的数据为：{{fromChildData}}</p>
    </div>
</template>
<script>
import child from './child'
export default {
    data() {
        return {
            fromChildData: ''
        }
    },
    components:{
        child
    },
    methods: {
        /** 
         * 第四步
         * 响应事件的参数为子组件传递过来的值
        */
        showMsgFromChild(data) {
            this.fromChildData = data
        }
    }
}
</script>
```

#### 方法2：父访问子： $children、 $ref  / 子访问父：$parent、$root

**$children的使用：**

this.$children返回的数据是**数组**类型，包含所有的子组件对象，可以通过遍历访问到所有子组件的message状态。需要注意**$children并不保证顺序**，也不是响应式的。

```js
console.log(this.$children[0].msg)
```

缺陷：通过该方法访问子组件时，访问每一个子组件必须通过索引值。但是当子组件过多时，我们不能确定想要的子组件的索引，甚至拿到后索引值也可能会发生变化，所以不推荐该方法

**$refs的使用：**

$refs以**对象结构**保存所有的子组件，通过给每个子组件一个ref（reference：引用）属性，即可访问特定子组件

```js
//父组件
 <son1 ref="child1"></son1>
 <son2 ref="child2"></son2>
 <son3 ref="child3"></son3>

//在生命周期函数mounted中使用
mounted(){
    console.log(this.$refs.child1.chimsg) //可以发现是访问指定的子组件，而不是通过索引
}

```

**$parent的使用：**

通过$parent访问到的是上一级父组件的实例，可以使用$root来访问根组件的实例。在子组件中直接调用即可

```js
//在生命周期的created阶段调用，因为在beforecreate阶段data数据还并未加载
// 在son3组件中：
  created(){
            //读取父组件数据
            this.son3msg = this.$parent.msg
            // console.log(this.son3msg)
    }
```

缺陷：在真实开发中很少通过$parent组件访问父组件，因为这样做耦合度太高了。并且如果将子组件放在另外一个组件内，可能父组件会发生变化，新的父组件中没有子组件要求的属性，这会产生一系列bug。另外，通过$parent直接修改父组件中的状态，那么父组件中的状态会变得飘忽不定，不利于后续的调试和维护.

**$root的使用：**

表示单一对象，当前组件树的根 Vue 实例，即new Vue({...根组件内容})。如果当前实例没有父实例，此实例将会是其自己。

#### 方法3：Eventbus（$emit、$on）- 兄弟组件传值

这种方法通过一个空的 Vue 实例作为中央事件总线（事件中心），用它来触发事件和监听事件,巧妙而轻量地实现了任何组件间的通信，**包括父子、兄弟、跨级**。（只在vue 2.X 中使用,vue 3.X中删除该方法，该使用mitt）。适用于中小型项目。当我们的项目比较大时，可以选择更好的状态管理解决方案 vuex。

```js
//1. 新建一个evenuBus.js，//因为是全局的一个'仓库'，所以初始化要在全局初始化，并暴露给全局
import Vue from 'vue';
export default new Vue();


//2. 向eventbus中传递数据，可通过按钮绑定一个方法,在发送数据的组件中：
import bus from "../utils/eventBus.js"
  methods:{
      sendmsg(){
             bus.$emit("sharedata", this.chimsg)
       }
  },

//3. 接收eventbus中的数据
import bus from "../utils/eventBus.js"
  created(){                     // 必须在created即以后的生命周期中接收，因为beforecreated中并未渲染好data等属性
       bus.$on("sharedata",val =>{
       this.child3msg = val
    })
 }
```

#### 方法4：mitt

- Vue2.x使用EventBus进行组件通信，而Vue3.x推荐使用mitt.js。

- 这是一种第三方库，使用npm 安装mitt足够小，仅有200bytes，其次支持全部事件的监听和批量移除，它还不依赖Vue实例，所以可以跨框架使用，React或者Vue，甚至jQuery项目都能使用同一套库。使用方法和eventbus非常相似

```js
//1. 新建一个mitt.js，//因为是全局的一个'仓库'，所以初始化要在全局初始化，并暴露给全局
import mitt from "mitt";
export default new mitt()

//2. 分别在son2和son3组件中引入暴露的mitt
import VueEvent from '../../utils/mitt'

//3. 向mitt中传递数据（son2组件中）
 methods:{
            sendmsg(){
                VueEvent.emit("sharedata",this.chimsg)
            }
  },

//4. 接收mitt中的数据（son3组件中）
 created()
            VueEvent.on("sharedata", val=>{
                this.child3msg = val
            })
 }  
```

#### 方法5： provide / inject（跨级 依赖注入）

这种方式就是Vue中的依赖注入，该方法以允许一个祖先组件向其所有子孙后代注入一个依赖，不论组件层次有多深，并在起上下游关系成立的时间里始终生效。在层数很深的情况下，可以使用这种方法来进行传值。就不用一层一层的传递了。

provide / inject是Vue提供的两个钩子，和data、methods是同级的。并且provide的书写形式和data一样。
●  provide 钩子用来发送数据或方法
●  inject 钩子用来接收数据或方法

```js
//父组件中
provide() {
 return {
    num: this.num,
    //传递方法也可以 
  };
}

//子组件中
inject: ['num']
//使用时this.num即可
```

#### **方法6： $attrs / $listeners（跨级）**

 跨级：多级组件嵌套需要传递数据时，通常使用的方法是通过 vuex。但如果仅仅是传递数据，而不做中间处理，使用 vuex 处理，未免有点大材小用。为此 Vue2.4 版本提供了另一种方法—— $attrs / $listeners

#### 方法7：特殊情况下使用v-model

一般情况,咱们使用v-model主要是用于数据的双向绑定,可以十分方便的获取到用户的输入值。但在某些特殊情况下,我们也可以将v-model用于父子组件之间的数据的双向绑定。这里需要用到父子传值的相关知识:

```js
//--------------------------父组件------------------------------------------
<template>
  <div>
    <son v-model="num"/> //使用子组件
  </div>
</template>

<script>
import son from '@/yanshi/son.vue'   //引入子组件
export default {
  components: {
    son    //注册子组件
  },
  data() {
    return {
      num: 100
    }
  }
}
</script>

//--------------------------子组件------------------------------------------
<template>
  <div>
    我是son组件里面接收到的值: {{ value }}
  </div>
</template>

<script>
export default {
  props: {
    value: {              //需要在子组件中接收父组件的值，接收的值必须写成value，其他值无法使用
      type: Number,
      required: true
    }
  }
}
</script>

//若想再修改子组件的props值时，使用$emit将其提交回父组件中，或将props中的值赋值给子组件中的data
```

#### 方法8： Vuex

回答思路：是什么 =》 包含内容=》为了解决什么问题=》特点 =》使用场景

**定义：**vuex是一个**状态管理机制**,采用**集中式存储**应用所有组件的状态。适用于父子、隔代、兄弟组件通信。VUEX提供了在多个组件间共享状态的插件，它包含着你的应用中大部分的状态 ( state )，且**store是响应式**的。当 Vue 组件从 store 中读取状态的时候，若 store 中的状态发生变化，那么相应的组件也会相应地得到高效更新。

- Vuex 的状态存储是响应式的。当 Vue 组件从 store 中读取状态的时候，若 store 中的状态发生变化，那么相应的组件也会相应地得到高效更新。
- 改变 store 中的状态的唯一途径就是显式地提交 (commit) mutation。这样可以方便地跟踪每一个状态的变化。

（通过`vue.prototype = XX`也可以使多个组件读取到共同的变量，但是这样并不是响应式的）

>状态管理：主要是将多个组件共享的变量全部存储在一个对象中，将这个对象放在顶层的VUE实例中，让其他组件可以使用。但是自己封装的对象做到响应式比较麻烦
>
>单一状态树：用一个对象就包含了全部的应用层级状态。
>
>- state => 基本数据(数据源存放地)
>- getters => state数据对象读取方法
>- mutations => ∶状态改变操作方法。是Vuex修改state的唯一推荐方法，其他修改方式在严格模式下将会报错。该方法只能进行同步操作，且方法名只能全局唯一。操作之中会有一些hook暴露出来，以进行state的监控等。
>- actions => 操作行为处理模块。负**责处理Vue Components接收到的所有交互行为。包含同步/异步操作，支持多个同名方法**，按照注册的顺序依次触发。向后台API请求的操作就在这个模块中进行，包括触发其他action以及提交mutation的操作。该模块提供了Promise的封装，以支持action的链式触发。
>- modules => 模块化Vuex

Vuex的响应式规则：

- 提前在state初始化好所需要的属性
- 当给state中的对象添加新属性时，使用Vue.set(obj, ‘newProp’, 123)

**使用场景：**

- 多个状态在多个界面间的共享问题
- 比如用户的登录状态，用户名称，头像，地理位置，商品收藏，购物车的物品等等
- 这些状态信息可以放在统一的地方，对他们进行保存和管理，并且他们还是响应式的

**项目结构：**

<img src="C:\Users\SFONE\AppData\Roaming\Typora\typora-user-images\image-20220606162053159.png" alt="image-20220606162053159" style="zoom:60%;" /><img src="C:\Users\SFONE\AppData\Roaming\Typora\typora-user-images\image-20220606163328936.png" alt="image-20220606163328936" style="zoom:60%;" />

**2.vuex主要包括以下五个模块/属性**

**1.State**：定义了应用状态的数据结构，可以在这里设置默认的初始状态。（基本数据(数据源存放地)）。Vuex使用了单一状态树管理应用层级别的全部状态，让我们能最直接的找到某个状态的片段，方便管理和维护，即在一个项目的store中只有一个state

**2.Getter**：允许**组件从 Store 中获取数据**，mapGetters 辅助函数仅仅是将 store 中的 getter 映射到局部计算属性。（从基本数据派生出来的数据）

应用场景：在Store仓库里，state就是用来存放数据，若是对数据进行处理输出，比如数据要过滤，一般我们可以写到computed中。但是如果很多组件都使用这个过滤后的数据，比如饼状图组件和曲线图组件，则可以把这个数据抽提出来共享，使用store中的计算属性getters
Getters中的参数：返回一个函数（状态在变）

<img src="C:\Users\SFONE\AppData\Roaming\Typora\typora-user-images\image-20220304201809157.png" alt="image-20220304201809157" style="zoom:200%;" />

**3.Mutation**：是**唯一**更改 state的方法，且必须是**同步函数**。（提交更改数据的方法，同步！）其**余组件通过commit获得mutation中的方法**。

可以通过浏览器插件devtools捕获mutation每一次的数据修改记录，定位到异常组件中

```js
//sotre/index.js文件中
const store = new Vuex.Store({
    state:{
        counter:0,
        students:[
            {id:1, age: 18, name:'aaa'},
            {id:2, age: 15, name:'bbb'},
            {id:3, age: 23, name:'ccc'},
            {id:4, age: 16, name:'ddd'},
            {id:5, age: 21, name:'eee'},
        ]

    },
    mutations:{  //自定义事件类型
        increment(state){     //默认传入参数state
            state.counter++
        },
        decrement(state){
            state.counter--
        },
        add(state,count){              //接收普通参数
            state.counter += count
        },
        addstudent(state,stu){
            state.student.push(stu)   //接收对象参数
        }

    }
})

//剩余组件使用mutation中的方法
 <button @click="subtraction">-</button>
 <button @click="addition">+</button>
  methods:{
            sendmsg(){
                // bus.$emit("sharedata", this.chimsg)  //VUE3中不支持eventbus
                VueEvent.emit("sharedata",this.chimsg)
            },
            addition(){
                this.$store.commit('increment')   //通过commit的方式获得方法,不传递参数
           		this.$store.commit('add',count)   //传递普通参数
            },
            subtraction(){
                this.$store.commit('decrement')
            },
            addstudent(){
                 const stu = {id:6, age: 20, name:'ddd'},
                 this.$store.commit('addstudent',stu)
            }
        },
```

**4.Action:** 而Action类似于mutation，不同点在于：

- Action 可以包含任意异步操作。
- Action 提交的是 mutation，而不是直接变更状态。Actions通过触发dispatch方法，通过mutation来改变state。可以进行**异步操作，即发送网络请求时。**Action还提供了promise的封装，支持action的链式触发

Action 函数接受一个**与 store 实例具有相同方法和属性的 context 对象**，因此你可以调用 context.commit 提交一个 mutation，或者通过 context.state 和 context.getters 来获取 state 和 getters。
所以，两者的不同点如下：

- Mutation专注于修改State，理论上是修改State的唯一途径；Action包含了业务代码、异步请求。
- Mutation：必须同步执行；Action：可以异步，但不能直接操作State。
- 在视图更新时，先触发actions，actions再触发mutation
- mutation的参数是state，它包含store中的数据；store的参数是context，它是 state 的父级，包含 state、getters

```js
// store/index.js
actions:{   //自定义异步方法,默认参数为context，表示上下文，只能进行异步操作，且不能直接修改state中的数据内容
        // aupdate( context ,payload){  //传递参数
        //     setTimeout(()=>{
        //         context.commit('update')
        //         console.log(payload.amsg);    //整体写法不够优雅
        //         payload.success()
        //     },1000)
        // }

        aupdate(context,payload){                 //payload是要传递的参数
            return new Promise((resolve, reject)=>{    //在action中return一个promise对象
                setTimeout(()=>{
                    context.commit('update');      //通过执行:commit()来触发 mutation 的调用, 间接更新 state
                    console.log(payload)
                    resolve()
                },1000)
            })
        }
    },
        
 //在VUE组件中： 使用action中某个方法返回的promise对象
    updateimg(){
        this.$store.dispatch('aupdate',        //向action中通过dispatch触发action中的异步事件,aupdate返回的是一个promise对象
        {                                //大括号整个是第二个参数payload
                amsg:'我是携带的信息',
                success:()=>{
                   console.log('已经完成了')
            	}
         }).then(res =>{
                    console.log('里面完成了提交')
                    console.log(res);
                })
     } 
```

**5.Module**：

背景：Vue使用单一状态树，意味着很多状态都会交给Vuex来管理。当应用变得非常复杂时，store对象就有可能变得非常臃肿。为了解决这个问题，Vuex允许我们将store分割为模块（Module），而每个模块拥有自己的state，mutation，action，getters等。

```js
//store/index.js
const moduleA ={  //自己封装模块
    state:{
        name:'zy'
    },
    mutations:{
        updataname(state,payload){       //内部函数的写法和正常的一样
            state.name = payload
        }
    },
    actions:{
		aUpdateName(context){     
            setTimeout(()=>{
                context.commit('updateNmae','wangsong')   //此时commit的是moduleA中的mutations，而不是根store中的mutations
            },1000)
        }
    },
    getters:{
        fullname(stste,payload){
            return stste.name + payload   
        },
		fullname2(state,getters){
            return getters.fullname + '222'   //可以调用上一个函数的返回值
        },
        fullname3(state,getters,rootState){
            return getters.fullname2 + rootState.counter   //通过rootState的方式调用根store中stare中的数据
        }
    }
}

//store里直接应用即可
 modules:{
        a:moduleA，
        b:modulsB
 }

//VUE组件中，直接调用，不需要加入自己封装模块的前缀名，不关心定义的位置，直接从store中调用。例：
<h1> {{ $store.state.a.name }} </h1>    //zy
<h1> {{ $store.getters.fullname }}</h1>
```

**这将单一的Store 拆分为多个 store 且同时保存在单一的状态树中，模块化vuex。**

**总结：**Vuex实现了一个单项数据流，在state中存储数据，并且只能通过mutations来修改state中的数据。组件中直接使用commit触发同步函数，使用dispatch触发异步函数。

### 3.VUEX的使用

1. 安装插件

2. 新建在store文件夹，在其目录下的indexjs中调用，并设置store对象，最后导出store，并在main.js中挂载（import store from ‘./store’）

   ```js
   //----------------store/index.js--------------------------------
   createApp(App)   //VUE3.X
       .use(Vuex)
   
   const store = new Vuex.Store({
       state:{
        ...
       },
       mutations:{ 
          ...
       },
       actions:{
           ...
       },
       getters:{
           ...
       },
       modules:{
           ...
       }
   })
           
   export default store
           
           
   //-----------main.js---------------------------------        
   ```

3. 在组件中使用state

```js
   <h2> {{ $store.state.counter }} </h2>

//使用 this.$store.commit('fn')调用同步函数，在methods中赋值自定义事件
subtraction(){
    this.$store.commit('decrement')   //commit只向mutation中提交
},

//使用 this.$store.dispatch('fn') 调用异步函数，在methods中赋值自定义事件
 addition(){
     this.$store.dispatch('aupdate',        //向action中提交,audate返回的是一个promise对象
          {                                //大括号整个是第二个参数payload
              amsg:'我是携带的信息',
              success:()=>{
             	 console.log('已经完成了')
          	  }
           })
           .then(res =>{
               console.log('里面完成了提交')
               console.log(res);
            })
 },
```

#### 1.Vuex为什么要分模块并且加命名空间？

**模块**：由于使用单一状态树，应用的所有状态会集中到一个比较大的对象。当应用变得非常复杂时，store 对象就有可能会变得相当臃肿。为了解决以上问题，Vuex 允许我们将 store 分割成模块（module）。每个模块拥有自己的 state、mutation、action、getter、甚至是嵌套子模块。

**命名空间**： 默认情况下，模块内部的 action、mutation、getter是注册在全局命名空间的 --- 这样使得多个模块能够对同一 mutation 或 action 做出响应。如果希望你的模块具有更高的封装度和复用性，你可以通过添加 namespaced:true 的方式使其成为带命名的模块。当模块被注册后，他所有 getter、action、及mutation 都会自动根据模块注册的路径调整命名。

#### 2.Vuex的应用场景分析

Vuex主要是为了提供多个组件共享状态的插件，并且能做到响应式。涉及到非父子关系的组件，例如兄弟关系、祖孙关系，甚至更远的关系组件之间的联系
中大型单页应用，可以更好地在组件外部管理状态。

- 登录用户的头像，名称，密码等用户的个人信息管理模块
- 商品收藏，购物车中的物品等状态信息，我的订单模块，订单列表也点击取消订单，然后更新对应的订单列表，这种情况也是用Vuex，state储存一个状态，监听这个状态，变化时更新对应的列表；
- 从订单结算页，进入选择优惠券的页面，选择优惠券的页面如何保存选择的优惠券信息？state保存优惠券信息，选择优惠券时，mutations提交，在订单结算页，获取选择的优惠券，并更新订单优惠信息

>**重要补充：**Vue实现用户登录及token验证：
>
>在前后端完全分离的情况下，Vue项目中实现token验证大致思路如下：
>
>1、第一次登录的时候，前端调后端的登陆接口，发送用户名和密码
>
>2、后端收到请求，验证用户名和密码，验证成功，就给前端返回一个token;验证失败，则返回失败信息
>
>3、前端拿到token，将token存储到localStorage和vuex中，并跳转路由页面
>
>4、前端每次跳转路由，就判断 localStroage 中有无 token ，没有就跳转到登录页面，有则跳转到对应路由页面
>
>5、每次调后端接口，都要在请求头中加token
>
>6、后端判断请求头中有无token，有token，就拿到token并验证token，验证成功就返回数据，验证失败（例如：token过期）就返回401，请求头中没有token也返回401
>
>7、如果前端拿到状态码为401，就清除token信息并跳转到登录页面

```js
// 添加请求拦截器，在请求头中加token
axios.interceptors.request.use(
config => {
  if (localStorage.getItem('Authorization')) {
    config.headers.Authorization = localStorage.getItem('Authorization');
  }

  return config;
},
error => {
  return Promise.reject(error);
});
```

#### 3.Vuex中mutations和actions的区别

- mutation中的操作是一系列的同步函数，用于**修改state中的变量的唯一入口**。当使用vuex时需要通过commit来提交需要操作的内容。只能通过mutation修改state中的内容

- action可以包含任意异步操作，不能直接修改state中变量的状态。当使用时必须通过dispatch，再触发mutation修改state中的变量。Action支持返回promise对象，可以进行链式调用

#### 4.为什么 Vuex 的 mutation 中不能做异步操作？

- Vuex中所有的状态更新的唯一途径都是mutation，异步操作通过 Action 来提交 mutation实现，这样可以方便地跟踪每一个状态的变化，从而能够实现一些工具帮助更好地了解我们的应用。
- 每个mutation执行完成后都会对应到一个新的状态变更，这样**devtools就可以打个快照存下来**，然后就可以实现 time-travel 了。如果mutation支持异步操作，就**没有办法知道状态是何时更新的，无法很好的进行状态的追踪**，给调试带来困难

#### 5.Vuex与localstorage

>localStorage是H5提供的一个更简单的数据存储方式，之前是用cookie存放数据，但是cookie的数据量太小，所以就用localStorage，它可以有5M的限制，不受刷新页面的控制，长久保存。

1. vuex 存储在**内存**，localstorage 以文件的方式存储在**本地**，**localstorage 只能存储字符串类型的数据**，储存对象需要JSON的Stringify 和 parse 方法进行处理，读取内存比读取硬盘速度要快（stringify：将js对象序列化为json字符串     parse：将json字符串解析为js对象）
2. vuex 是一个专为vue.js 应用程序开发的状态管理模式，它采用集中式管理应用的所有组件状态，并以相应的规则保证状态的以一种可以预测的方式发生变化，**vuex 用于组件之间的传值**；localstorage 是本地储存，是将**数据存储到浏览器**的方法，一般在**跨页面传递数据**时使用。
3. vuex能够做到数据的响应式，localstorage 不能
4. 永久性：刷新页面时vuex存储的值会丢失，localstorage 不会

#### 6.Redux 和 Vuex 有什么区别，它们的共同思想

>Redux: 是一个十分常用的状态容器库，很小巧, 只有 2kb, 但是珍贵的是他的 `reducer` 和 `dispatch` 这种思想方式，主要应用于react中
>
>Redux包括：
>
>- state：和vuex类似，是整个应用的数据。但是，并不是所有的数据都需要保存到state中，有些属于组件的数据是完全可以留给组件自身去维护的。
>- action：唯一改变state的方法救赎触发action。action 的本质是一个对象（同步action ，或借助 中间件，利用redux-thunk 实现异步操作，action 不会改变 store，只是描述了怎么改变store）
>
>![image-20220607143733496](C:\Users\SFONE\AppData\Roaming\Typora\typora-user-images\image-20220607143733496.png)
>
>- reducer： 纯函数，根据action和旧的store计算出新的store
>- store：维持应用的state；提供getState()方法获取 state；提供dispatch(action)方法更新 state；通过subscribe(listener)注册监听器; 通过subscribe(listener)返回的函数注销监听器。

**1.主要区别**

1. **VUEX弱化了dispatch的存在感**。VUEX认为状态变更的触发是一次“提交”而已，而调用方式则是框架提供一个提交的commit API接口。
2. **VUEX取消了Redux中Action的概念**。不同于Redux认为状态变更必须是由一次"行为"触发，VUEX仅仅认为在任何时候触发状态变化只需要进行mutation（转变）即可。Redux的Action必须是一个对象，而VUEX认为只要传递必要的参数即可，形式不做要求。
3. **VUEX也弱化了Redux中的reducer的概念**。reducer在计算机领域语义应该是"规约"，在这里意思应该是根据旧的state和Action的传入参数，"规约"出新的state。在VUEX中，对应的是mutation，即"转变"，只是根据入参对旧state进行"转变"而已。
4. VUEX支持getter，运行中是带缓存的，算是对提升性能方面做了些优化工作

<img src="C:\Users\SFONE\AppData\Roaming\Typora\typora-user-images\image-20220607144047207.png" alt="image-20220607144047207" style="zoom: 67%;" />

<img src="C:\Users\SFONE\AppData\Roaming\Typora\typora-user-images\image-20220607144100271.png" alt="image-20220607144100271" style="zoom:67%;" />

|                      | VUEX                                                | Redux                                                        |
| -------------------- | --------------------------------------------------- | ------------------------------------------------------------ |
| 核心对象             | store                                               | store                                                        |
| 数据存储             | state                                               | state                                                        |
| 状态更新提交接口     | commit                                              | dispatch                                                     |
| 状态更新提交参数     | 带type和payload的**mutation**，提交对象/参数        | 带type和payload的**action**（action是一个对象）              |
| 状态更新计算         | mutation handler                                    | reducer（纯函数）                                            |
| 限制                 | mutation handler必须是非异步方法                    | reducer必须是纯函数，不支持异步                              |
| 特性                 | 支持带缓存的getter，用于获取state经过某些计算后的值 | 支持中间件                                                   |
| 同步，异步操作的支持 | mutation支持同步操作； action支持异步操作           | action直接dispatch，支持同步操作；异步操作：使用中间件，先将异步操作dispatch到action creator中，操作结果放在action中，再次dispatch到reducer方法中 |

**2.共同思想**

- 单一数据源
- 变化可以预测
- 都使用了设计模式中的观察者模式或者说发布-订阅模式

本质上：redux与vuex都是对mvvm思想的服务，将数据从视图中抽离的一种方案;
形式上：vuex借鉴了redux，通过弱化概念，在任何东西都没做实质性削减的基础上，使得整套框架更易于理解了。并且vuex将store作为全局的数据中心，进行mode管理;

#### 7.为什么要使用Vuex或者redux？

由于**传参的方法对于多层嵌套的组件将会非常繁琐**，并且对于兄弟组件间的状态传递无能为力。我们经常会采用父子组件直接引用或者通过事件来变更和同步状态。以上的这些模式非常脆弱，通常会导致代码无法维护，浪费了带宽资源。所以需要把**组件的共享状态抽取**出来，以一个**全局单例模式**管理，只能通过mutation改变state中的数据，组件树构成了一个巨大的"视图"，不管在树的哪个位置，任何组件都能获取状态或者触发行为。

另外，通过定义和隔离状态管理中的各种概念并强制遵守一定的规则，代码将会变得更结构化且易维护。

#### 8.Vuex和单纯的全局对象有什么区别？

>全局变量一般放在global.js文件中，在js文件中export default{ XXX}导出

- Vuex 的状态存储是响应式的。当 Vue 组件从 store 中读取状态的时候，若 store 中的状态发生变化，那么相应的组件也会相应地得到高效更新。
- 不能直接改变 store 中的state。改变 store 中的状态的唯一途径就是显式地提交 (commit) mutation。这样可以方便地跟踪每一个状态的变化，从而能够实现一些工具帮助更好地了解我们的应用。
- vuex由统一的方法修改数据，全局变量可以任意修改数据

#### 9.Vuex中严格模式的作用和开启方式

在严格模式下，无论何时发生了状态变更且不是由mutation函数引起的，将会抛出错误。这能保证所有的状态变更都能被调试工具跟踪到。

```js

const store = new Vuex.Store({
    strict:true,  //在store下的index.js中，开启严格模式
    state:{},
    getters:{},
    ....
})
```

#### 10.mapState, mapGetter, mapMutation, 

mapState: 自动将需要的state值映射为该vue组件实例中的计算属性（使用…表示将mapstate映射的计算属性追加上去，而不是覆盖原有的）

```js
import { mapState } from 'vuex'
computed: {   
  value(){
   return this.val++
  },
  ...mapState(['likes','friends','token','userInfo'])

}

//我们映射的时候，想给计算属性起个新的名字,不想用原有的属性名，那就可以像下面这样做
computed: {   
  value(){
   return this.val++
  },
  ...mapState({
      myLikes:"likes",
      myFriends:"friends",
      theUserInfo:"userInfo"
  })
}
```

mapGetter:其主要用法也是一样的，也能将getters的属性映射到实例的计算属性。但是getter可以进行一些简单的筛选等，我们不想取所有的state里面的friends值，而是想根据我们传入的值筛选一下，则需要**在getter返回的值套上一层函数那我们就可以实现传参数**

```js
import { mapGetters} from 'vuex'
computed: {  
 valued(){
   return this.value++
 },
 ...mapGetters(['realName','myMoney'])
}
//也可以取别名，使用方法同上
```

mapMutation：mapMutations是**将所有mutations里面的方法**映射为实例methods里面的方法

```js
import { mapMutations } from 'vuex'

<button @click="addAge({number:1})">增加一岁</button>
methods:{
 ...mapMutations(['addAge'])
}
//上述操作等同于：
methods:{
 addAge(payLoad){
  this.$store.commit('addAge',payLoad)
 }
}

//更换名称：
<button @click="handleAddAge({number:1})">增加一岁</button>
methods:{
 ...mapMutations({
     handleAddAge:'addAge'
 })
}
```

### 4.怎样理解 Vue 的单向数据流？

**1.定义**

**单向数据流**，指的是数据只能从父组件向子组件传递，子组件内部，不能直接修改父组件传递过来的`props`—`props`中的内容是只读的。如果想要修改只能通过`emit`事件触发的方式，在父组件中修改。**防止多个子组件都尝试修改父组件状态时，让应用中的数据流变得难以追溯。**

额外的，每次父级组件发生更新时，子组件中所有的 prop 都将会刷新为最新的值。这意味着你不应该在一个子组件内部改变 prop。如果你这样做了，Vue 可能会在浏览器的控制台中发出警告（分为基本类型props和引用props）。子组件想修改时，只能通过 $emit 派发一个自定义事件，父组件接收到后，由父组件修改。

**如果子组件改了`props`的值会怎么样呢？**这里分情况讨论：

1. 如果子组件修改的`props`数据类型，是引用数据类型，那么绑定的其实是引用地址，子组件修这个引用类型的值，vue不会报警告，但是建议别这样做。

2. 如果绑定的`props`是基础类型值，子组件直接修改父组件传递的`props`，vue会抛出警告。

   ![img](https://img-blog.csdnimg.cn/d198256d0e6c4f4080f6653ff47ca643.png)

所以，尽量使用单向数据流，这样做的优点是：

1. 单向数据流会使所有状态的改变可记录、可跟踪，源头易追溯；
2. 所有数据只有一份，组件数据只有唯一的入口和出口，使得程序更直观更容易理解，有利于应用的可维护性。

### 5.VUE中封装的数组方法和响应式监听

由于Object.defineProperty的监听对象是对象，所以vue源码里缓存了array的原型链，然后重写了这几个方法，触发这几个方法的时候会observer数据，意思是使用这些方法不用再进行额外的操作，视图自动进行更新，这些方法包括push,pop,shift,unshift,splice,sort,reverse。以下是js中对数组操作的源码：

```js
// 缓存数组原型
const arrayProto = Array.prototype;
// 实现 arrayMethods.__proto__ === Array.prototype
export const arrayMethods = Object.create(arrayProto);
// 需要进行功能拓展的方法
const methodsToPatch = [
  "push",
  "pop",
  "shift",
  "unshift",
  "splice",
  "sort",
  "reverse"
];

/**
 * Intercept mutating methods and emit events
 */
methodsToPatch.forEach(function(method) {
  // 缓存原生数组方法
  const original = arrayProto[method];
  def(arrayMethods, method, function mutator(...args) {
    // 执行并缓存原生数组功能
    const result = original.apply(this, args);
    // 响应式处理
    const ob = this.__ob__;
    let inserted;
    switch (method) {
    // push、unshift会新增索引，所以要手动observer
      case "push":
      case "unshift":
        inserted = args;
        break;
      // splice方法，如果传入了第三个参数，也会有索引加入，也要手动observer。
      case "splice":
        inserted = args.slice(2);
        break;
    }
    // 
    if (inserted) ob.observeArray(inserted);// 获取插入的值，并设置响应式监听
    // notify change
    ob.dep.notify();// 通知依赖更新
    // 返回原生数组方法的执行结果
    return result;
  });
});
```

简单来说就是，重写了数组中的那些原生方法，首先获取到这个数组的__ob__，也就是它的Observer对象，如果有新的值，就调用observeArray继续对新的值观察变化（也就是通过target__proto__ == arrayMethods来改变了数组实例的型），然后手动调用notify，通知渲染watcher，执行update。

### 6.vue组件中data为什么必须是一个函数？

当一个组件被定义后，可能用于创建多个实例。如果组件里 data 直接写了一个对象的话，那么如果你在模板中多次声明这个组件，组件中的 data 会指向同一个引用，因此，无论在哪个组件实例中修改了data,都会污染其他组件中的data。 而如果使用函数的话，数据以函数返回值形式定义，每个组件里的data会有单独的引用。这样每复用一次组件，就会返回一份新的data，类似于给每个组件实例创建一个私有的数据空间，让各个组件实例维护各自的数据。

### 7.Vue组件可以访问Vue实例数据吗？

答：不可以，组件是一个单独功能模块的封装，这个模块有属于自己的html模板，也应该有属于自己数据保存的地方。即使可以访问，所有的数据都放在Vue实例中，Vue实例就会变得非常臃肿。

### 8.params和query的区别

答：用法：query要用path来引入，params要用name来引入，接收参数都是类似的，分别是this.$route.query.name和this.$route.params.name。

url地址显示：query更加类似于我们ajax中get传参，params则类似于post，说的再简单一点，前者在浏览器地址栏中显示参数，后者则不显示

注意点：query刷新不会丢失query里面的数据

params刷新会丢失params里面的数据。

### 9.Vue.js中ajax请求代码应该写在组件的methods中还是vuex的actions中？

答：如果请求来的数据是不是要被其他组件公用，仅仅在请求的组件内使用，就不需要放入vuex 的state里。

如果被其他地方复用，这个很大几率上是需要的，如果需要，请将请求放入action里，方便复用。

### 10.Proxy 与 Object.define Property 优劣对比

Proxy 的优势如下:

Proxy 可以直接监听对象而非属性；

Proxy 可以直接监听数组的变化；

Proxy 有多达 13 种拦截方法,不限于 apply、ownKeys、deleteProperty、has 等等是 Object.defineProperty 不具备的；

Proxy 返回的是一个新对象,我们可以只操作新的对象达到目的,而 Object.defineProperty 只能遍历对象属性直接修改；

Proxy 作为新标准将受到浏览器厂商重点持续的性能优化，也就是传说中的新标准的性能红利；

Object.defineProperty 的优势如下:

兼容性好，支持 IE9，而 Proxy 的存在浏览器兼容性问题,而且无法用 polyfill 磨平，因此 Vue 的作者才声明需要等到下个大版本( 3.0 )才能用 Proxy 重写。

### 11.什么是前端渲染？什么是后端渲染？

1）第一阶段：

后端渲染：jsp/java等服务器

后端路由：处理URL和页面之间的映射关系

后端路由缺点：整个页面模块都又后端人员编写和维护，前端人员如果想要开发界面，需要通过php、java等编写页面代码，此时，html代码和数据以及对应逻辑会混在一起，编写与维护非常困难

2）第二阶段：

前端渲染：浏览器中显示的网页中的大部分内容，都是由前端写的js代码在浏览器中执行，最终渲染出来界面。后端只提供API来返回数据，前端通过ajax获取数据，通过js将数据渲染到网页。

前端渲染优点：前后端责任清洗，后端专注于数据，前端专注于交互和可视化。当移动端出现后，后端不需要任何处理，依然使用之前的一套API即可

3）第三阶段：

单页面富应用（SPA）阶段：SPA最主要的特点是在前后端分离的基础上加了一层前端路由，由前端来维护一套路由规则。静态资源服务器中只有一个html界面

此时，URL和页面的映射关系为前端路由（vue-router）。前端路由的核心是指改变URL，但页面不进行整体的刷新

### 11.使用过 Vue SSR 吗？说说 SSR？

**定义：**SSR也指服务端渲染，也就是将Vue在客户端把标签渲染成HTML的工作放在服务端完成，然后再把html直接返回给客户端。就是vue在客户端将标签渲染成的整个 html 片段的工作在服务端完成，服务端形成的html 片段直接返回给客户端这个过程就叫做服务端渲染。

**（1）SSR的优点：**

- **更好的 SEO**：不同爬虫工作原理类似，只会爬取源码，不会执行网站的任何脚本（Google除外，据说Googlebot可以运行javaScript）。使用了Vue或者其它MVVM框架之后，页面大多数DOM元素都是在客户端根据js动态生成，可供爬虫抓取分析的内容大大减少。另外，浏览器爬虫不会等待我们的数据完成之后再去抓取我们的页面数据。服务端渲染返回给客户端的是已经获取了异步数据并执行JavaScript脚本的最终HTML，网络爬中就可以抓取到完整页面的信息。
- **更快的内容到达时间（首屏加载更快）**：SPA 会等待所有 Vue 编译后的 js 文件都下载完成后，才开始进行页面的渲染，文件下载等需要一定的时间等，所以首屏渲染需要一定的时间。而在SSR中，首屏的渲染是node发送过来的html字符串，并不依赖于js文件了，这就会使用户更快的看到页面的内容。尤其是针对大型单页应用，打包后文件体积比较大，普通客户端渲染加载所有所需文件时间较长，首页就会有一个很长的白屏等待时间。

**（2) SSR的缺点：**

- **更多的开发条件限制**：在服务端渲染中，created和beforeCreate之外的生命周期钩子不可用，因此项目引用的第三方的库也不可用其它生命周期钩子，这对引用库的选择产生了很大的限制；
- **更多的服务器负载**：本来是通过客户端完成渲染，现在统一到服务端node服务去做。尤其是高并发访问的情况，会大量占用服务端CPU资源；显然会比仅仅提供静态文件的 server 更加大量占用CPU 资源 。因此如果你预料在高流量环境 ( high traffic ) 下使用，请准备相应的服务器负载，并明智地采用缓存策略。
- **学习成本相对较高**：除了对webpack、Vue要熟悉，还需要掌握node、Express相关技术。相对于客户端渲染，项目构建、部署过程更加复杂。

### 12.为什么使用axios ?

​	vue发送网络请求的方式有很多种，分析其利弊

1. 传统ajax基于XMLHttpRequest(XHR)

   不用原因：配置和调用方式比较混乱，编码起来很麻烦

2. 使用jquery-ajax

   相对于传统ajax很好用，但是在Vue整个开发中都不需要使用jquery了，juqery代码1w+，Vue代码也是1w+，没必要为了网络请求二引用这个重量级框架

3. vue-resource：

   相对于juqery小了很多，是官方退出的，但是在VUE2.0推出后，作者表明去掉了该方法并表示不会再更新，无人维护

4. 作者推荐使用axios，在浏览器中发送XMLHttpRequest请求，在node.js中发送http请求，支持Promise API，拦截请求和相应，转换请求和相应等

### 14. axios的使用

>Axios 是一个基于 promise 的 HTTP 库，可以用在浏览器和 node.js 中。
>从浏览器中创建 XMLHttpRequests
>从 node.js 创建 http 请求
>支持 Promise API
>拦截请求和响应
>转换请求数据和响应数据
>取消请求
>自动转换 JSON 数据
>客户端支持防御 XSRF
>
>- 实际上，axios可以用在浏览器和 node.js 中是因为，它会自动判断当前环境是什么，如果是浏览器，就会基于**XMLHttpRequests**实现axios。如果是node.js环境，就会**基于node内置核心模块http**实现axios。并使用promise对象来对结果进行处理

```js
// 1.安装: npm install axios –save

// 2.导入: import axiso from ‘axios’
axios({
​	url:'http://.....' ,     
    methods: 'get'，
    params:{					   //在get请求中，如果不想把文件名直接拼接在URL后，可使用参数拼接，即top
    	type:'pop',             
    	page:1
	}

}).then(res=>{
    console.log(res)               //res表示拿到的结果
}) 


//axios.create使用方法
cosnt instance = axios.create({
    baseURL:'http://localhost:8080/' //基础路径
})

instance({
	url: '/login',
    method: 'POST',    //可以实现自动拼接等
    data: res
})
// 1.可以简化路径写法 2.当基础路径发生变化时方便修改，有利于维护
```

### 15.axios发送并发请求与全局配置

答：有时候需求需要同时发送两个请求，且必须同时到达时，使用axios的all（）方法

```js
//3. axios发送并发请求
axios.all([axios({             //axios.all方法可以放入多个请求的数组
    url:'http://11111'
}),axios({
    url:'http://22222'
    params:{
    type:'sell',                  
    page:5
}
})]).then(axios.spread(request1,request2) =>{        //axios.spread可以将数组【res1，res2】展开为res1，res2
    console.log(request1)
})

//4. axios的全局配置
axios.default.baseURL = 'HTTP://1111',
axios.default.timeout = 5000
```

axios的常用配置信息

<img src="C:\Users\SFONE\AppData\Roaming\Typora\typora-user-images\image-20220304211157380.png" alt="image-20220304211157380" style="zoom:80%;" />

### 16.axios的实例和模块封装

>封装axios的原因：
>
>大型项目中，对Http的请求有很多，且需要区分环境，每个网络请求有相似需要处理的部分，如果不封装相同的功能，可能会造成代码冗余，破坏工程的可复用性，扩展性。并且不同的项目需要不同的axios功能

**流程：设置基本基本的配置信息（URL,Port，Time等）-> 创建axios实例 ->封装实例中的功能（拦截请求，相应请求，修改请求头等功能） -> 导出实例 -> 封装实例为api接口  ->  在实际的vue组件中使用axios实例对应的接口** 

```js
//1.在HTTP/config/config.js中配置基本信息
const serverConfig = {
  baseURL: "https://smallpig.site", // 请求基础地址,可根据环境自定义
  useTokenAuthorization: true, // 是否开启 token 认证
};
export default serverConfig;

//2.在HTTP/index.js中封装相应的功能
//创建axios的实例
const serviceAxios = axios.create({
    baseURL:serverConfig.baseURL,    //引用设置好的config中的数据信息
    timeout:5000,
})

//请求拦截相关业务需求
serviceAxios.interceptors.request.use(
   (config) => {   //相应成功后的一些配置，包括请求头设置，序列化数据等业务需求
    // 如果开启 token 认证
    if (serverConfig.useTokenAuthorization) {
      config.headers["Authorization"] = localStorage.getItem("token"); // 请求头携带 token
    }else{
        //跳转路由登录等功能
      this.$router.push("/elseDetail");
    }
    // 设置请求头
    if(!config.headers["content-type"]) { // 如果没有设置请求头
      if(config.method === 'post') {
        config.headers["content-type"] = "application/x-www-form-urlencoded"; // post 请求
        config.data = qs.stringify(config.data); // 序列化,比如表单数据
      } else {
        config.headers["content-type"] = "application/json"; // 默认类型
         
      }
    }
    console.log("请求配置", config);
    return config;     //成功的函数返回配置内容
  },
    (error) => {
        Promise.reject(error)    //若相应拦截失败，返回相应的业务逻辑
    }
    );

//响应拦截相关业务需求
serviceAxios.interceptors.response.use(
    (res)=>{
        console.log("响应拦截",res)   //处理拦截后的业务逻辑，比如判断token是否过期等
    },
    (error) =>{
       let message = "";
    if (error && error.response) {
      switch (error.response.status) {
        case 302:
          message = "接口重定向了！";
          break;
        case 400:
          message = "参数不正确！";
          break;
        case 401:
          message = "您未登录，或者登录已经超时，请先登录！";
          break;
        case 403:
          message = "您没有权限操作！";
          break;
        case 404:
          message = `请求地址出错: ${error.response.config.url}`;
          break;
        case 503:
         if(window.temp){
              window.temp=false;
              MessageBox.confirm('你的会话已失效', '确定登出', {
              confirmButtonText: '重新登录',
              cancelButtonText: '取消',
              type: 'warning',
          }).then(() => {
            window.temp=true;
            window.clearInterval(window.interval);    //清除计时器
            sessionStorage.removeItem('userInfo');    //清除用户信息
            // store.commit('logOut');    //注销
            location.reload(); // 为了重新实例化vue-router对象 避免bug
          }).catch(() => {       

          });    
        default:
          message = "异常问题，请联系管理员！";
          break;
      }
    }
)

export default serviceAxios   //导出封装好的实例

//在接口文件/api/index.js中使用封装好的axios实例
 import serviceAxios from "../index";

 const getUserInfo = (params) =>{
    return serviceAxios({
        method:'get',
        url:params,
        params,
    });
}

//post请求，一般返回表单数据
export const login = (data) => {
    return serviceAxios({
        url: "/api/user/login",
        method: "post",
        data,
        headers:{
            'content-type':'XXXX'
        }
    });
};
       
//Vue使用封装好的接口
import { login } from "@/http/api/user"
async loginAsync() {
  let params = {
    email: "123",
    password: "12321"
  }
  let data = await login(params);
  console.log(data);
}
```

按照不得过度依赖第三方框架的原则，需在一个文件夹中进行封装。新建一个文件夹network/request.js

```js
export function request(config){
    return new Promise((resolve,reject)=>{
        //创建axios实例
        const instance = axios.create({
            baseUrl:'http://1111',
            timeout:5000
        })
        
        //发送真正的网络请求
        return instance(config)
    })
}


//在文件其他位置使用时
request({
    url:'/home/test1'
}).then(res=>{
    console.log(res)
}).catch(err=>{
    console.log(err)
})
```

### 17.axios拦截器

共提供4中拦截器，请求成功/失败，响应成功/失败

```js
//axios请求拦截器
instance.interceptors.request.use(config=>{
    //例：修改config文件中的header，即config不符合服务器要求，登录时的token等
    if(config.url !=='/login'){
        config.headers.Authorization = sessionStorage.getItem('token')  //除了登录页面，都需要带token
    }
    return config   //必须返回，否则别人接收不到
}.err=>{
   	console.log(err)
})

//axios响应拦截器
instance.interceptors.response.use(res=>{
    xxx = res.data 
    //eject用于取消拦截器
    console.log(res)
}.err=>{
    
})
```

axios拦截器原理：

axios维护一个handlers数组，里面按照顺序存放着【请求拦截函数、api请求、响应拦截函数】，遍历执行handlers数组以达到一定的执行顺序

### 18.如何配置vue.config.js解决跨域问题

#### 1.原理

	- 将域名发送给本地的服务器
	- 再由本地服务器请求真正的服务器
	- 因为请求是从服务端发出的，所以不存在跨域的问题

#### 2.使用方法

```js
//1. 在vue.config.js文件中加入相应拦截
module.exports ={
  devServer:{   //配置跨域  
    proxy:{
      '/api':{            //api表示拦截以/api为开头的请求路径
        target:'https://www.vue-js.com/api',   //跨域的域名
        changeOrigin:true,   //是否开启跨域
        pathRewrite:{       //重写路径
          '^/api':''            //把/api变成空字符,可能出现域名重复，主要看target中的设置
        }
      }
    }
  }
}


//2. 在组件使用axios时，即可自动拦截，例，在APP组件中
<button @click=' handleClick ' > 发送数据请求 </button>

methods:{
    handleClick(){
        axios.get('api/v1/topics').then(res =>{
            console.log('数据请求成功')
            console.log(res)
        })
    }
}

```

### 21. Ajax，Fetch和Axios的异同

##### 1 AJAX

AJAX是 Asynchronous JavaScript and XML （异步的JavaScript和XML）的缩写，指的是通过 JavaScript 的 异步通信，从服务器获取 XML 文档从中提取数据，再更新当前网页的对应部分，而不用刷新整个网页，是一种**思想，XMLHttpRequest是实现ajax的一种方式**。通过在后台与服务器进行少量数据交换，**Ajax 可以使网页实现局部更新**。这意味着可以在不重新加载整个网页的情况下，对网页的某部分进行更新。传统的网页（不使用 Ajax）如果需要更新内容，必须重载整个网页页面。其缺点如下：

- 本身是针对MVC编程，不符合前端MVVM的浪潮
- 基于原生XHR开发，XHR本身的架构不清晰
- 不符合关注分离（Separation of Concerns）的原则
- 配置和调用方式非常混乱，而且基于事件的异步模型不友好。

>  MVC,MVP,MVVM是三种常见的前端架构模式(Architectural Pattern),它通过分离关注点来改进代码组织方式。不同于设计模式(Design Pattern),只是为了解决一类问题而总结出的抽象方法，一种架构模式往往能使用多种设计模式。
>
>  MVC模式是MVP,MVVM模式的基础，这两种模式更像是MVC模式的优化改良版,他们三个的MV即Model，view相同，不同的是MV之间的纽带部分。本文主要介绍MVC与MVVM的应用与区别，因为MVP好像不是很常用。

创建AJAX请求的步骤：

- **创建一个 XMLHttpRequest 对象。**
- 在这个对象上**使用 open 方法创建一个 HTTP 请求**，open 方法所需要的参数是请求的方法、请求的地址、是否异步和用户的认证信息。
- 在发起请求前，可以为这个对象**添加一些信息和监听函数**。比如说可以通过 setRequestHeader 方法来为请求添加头信息。还可以为这个对象添加一个状态监听函数。一个 XMLHttpRequest 对象一共有 5 个状态，当它的状态变化时会触发onreadystatechange 事件，可以通过设置监听函数，来处理请求成功后的结果。当对象的 readyState 变为 4 的时候，代表服务器返回的数据接收完成，这个时候可以通过判断请求的状态，如果状态是 2xx 或者 304 的话则代表返回正常。这个时候就可以通过 response 中的数据来对页面进行更新了。
- 当对象的属性和监听函数设置完成后，最后调**用 sent 方法来向服务器发起请求**，可以传入参数作为发送的数据体

```js
//1.利用XMLHttpRequest实现Ajax
   function ajax(url) {
      const xhr = new XMLHttpRequest();
      xhr.open("get", url, false);    
      xhr.onreadystatechange = function () {
        // 异步回调函数
        if (xhr.readyState === 4) {
          if (xhr.status === 200) {
            console.info("响应结果", xhr.response)
          }
        }
      }
      xhr.send(null);
    }
   ajax('https://smallpig.site/api/category/getCategory')

// promise 封装实现ajax：
function getJSON(url) {
  // 创建一个 promise 对象
  let promise = new Promise(function(resolve, reject) {
    let xhr = new XMLHttpRequest();
    // 新建一个 http 请求
    xhr.open("GET", url, true);
    // 设置状态的监听函数
    xhr.onreadystatechange = function() {
      if (this.readyState !== 4) return;
      // 当请求成功或失败时，改变 promise 的状态
      if (this.status === 200) {
        resolve(this.response);
      } else {
        reject(new Error(this.statusText));
      }
    };
    // 设置错误监听函数
    xhr.onerror = function() {
      reject(new Error(this.statusText));
    };
    // 设置响应的数据类型
    xhr.responseType = "json";
    // 设置请求头信息
    xhr.setRequestHeader("Accept", "application/json");
    // 发送 http 请求
    xhr.send(null);
  });
  return promise;
}
```

##### 2  Fetch

fetch号称是AJAX的替代品，是在ES6出现的，使用了ES6中的promise对象。Fetch是基于promise设计的。Fetch的代码结构比起ajax简单多。**fetch不是ajax的进一步封装，而是原生js，没有使用XMLHttpRequest对象**。

>Fetch是一个真实中存在的API，是基于Promise，而Ajax是一种思想，由XMLHttpRequest实现

fetch的优点：

- 语法简洁，更加语义化
- 基于标准 Promise 实现，支持 async/await
- 更加底层，提供的API丰富（request, response）
- 脱离了XHR，是ES规范里新的实现方式

fetch的缺点：

- fetch只对网络请求报错，对400，500都当做成功的请求，服务器返回 400，500 错误码时并不会 reject，只有网络错误这些导致请求不能完成时，fetch 才会被 reject。
- fetch默认不会带cookie，需要添加配置项： fetch(url, {credentials: 'include'})
- fetch不支持abort，不支持超时控制，使用setTimeout及Promise.reject的实现的超时控制并不能阻止请求过程继续在后台运行，造成了流量的浪费
- fetch没有办法原生监测请求的进度，而XHR可以

>特点：
>
>- 使用promise的链式调用，不使用回调函数
>- 采用模块化设计，比如rep，res等对象分散开来，比较友好
>- 通过**数据流**处理数据，提高了网页性能

```js
function ajaxFetch(url) {
    fetch(url).then(res => res.json()).then(data => {
       console.info(data)
    })
 }
 ajaxFetch('https://smallpig.site/api/category/getCategory')

```

##### 3 Axios

Axios 是一种基于Promise封装的网络请求库，是基于XHR的二次封装，其特点如下：

- 浏览器端发起XMLHttpRequests请求
- node端发起http请求
- 支持Promise API
- 监听请求和返回
- 对请求和返回进行转化
- 取消请求
- 自动转换json数据
- 客户端支持抵御XSRF攻击

可以说Axios是XHR的一个子集，而XHR又是Ajax的一个子集

```js
// 发送 POST 请求
axios({
    method: 'post',
    url: '/user/12345',
    data: {
        firstName: 'Fred',
        lastName: 'Flintstone'
    }
})

```

## 六、VUE路由相关

### 0.对前端路由的理解

在前端技术早期，一个 url 对应一个页面，如果要从 A 页面切换到 B 页面，那么必然伴随着页面的刷新。这个体验并不好，不过在最初也是无奈之举——用户只有在刷新页面的情况下，才可以重新去请求数据。

后来，改变发生了——Ajax 出现了，它允许人们在不刷新页面的情况下发起请求；与之共生的，还有“不刷新页面即可更新页面内容”这种需求。在这样的背景下，出现了 SPA（单页面应用）。

SPA极大地提升了用户体验，它允许页面在不刷新的情况下更新页面内容，使内容的切换更加流畅。但是在 SPA 诞生之初，人们并没有考虑到“定位”这个问题——在内容切换前后，页面的 URL 都是一样的，这就带来了两个问题：

- **SPA 其实并不知道当前的页面“进展到了哪一步”。**可能在一个站点下经过了反复的“前进”才终于唤出了某一块内容，但是此时只要刷新一下页面，一切就会被清零，必须重复之前的操作、才可以重新对内容进行定位——SPA 并不会“记住”你的操作。
- 由于有且仅有一个 URL 给页面做映射，这对 SEO 也不够友好，搜索引擎无法收集全面的信息

为了解决这个问题，前端路由出现了。

前端路由可以帮助我们在仅有一个页面的情况下，**“记住”用户当前走到了哪一步**—**—为 SPA 中的各个视图匹配一个唯一标识**。这意味着用户前进、后退触发的新内容，都会映射到不同的 URL 上去。此时即便他刷新页面，因为当前的 URL 可以标识出他所处的位置，因此内容也不会丢失。

那么如何实现这个目的呢？首先要解决两个问题：

- 当用户刷新页面时，浏览器会默认根据当前 URL 对资源进行重新定位（发送请求）。这个动作对 SPA 是不必要的，因为我们的 SPA 作为单页面，无论如何也只会有一个资源与之对应。此时若走正常的请求-刷新流程，反而会使用户的前进后退操作无法被记录。
- 单页面应用对服务端来说，就是一个URL、一套资源，那么如何做到用“不同的URL”来映射不同的视图内容呢？

从这两个问题来看，服务端已经完全救不了这个场景了。所以要靠咱们前端自力更生，不然怎么叫“前端路由”呢？作为前端，可以提供这样的解决思路：

- 拦截用户的刷新操作，避免服务端盲目响应、返回不符合预期的资源内容。把刷新这个动作完全放到前端逻辑里消化掉。
- 感知 URL 的变化。这里不是说要改造 URL、凭空制造出 N 个 URL 来。而是说 URL 还是那个 URL，只不过我们可以给它做一些微小的处理——这些处理并不会影响 URL 本身的性质，不会影响服务器对它的识别，只有我们前端感知的到。一旦我们感知到了，我们就根据这些变化、用 JS 去给它生成不同的内容。

### 1.vue-router是什么?它有哪些组件

答：Vue用来写路由一个插件。有router-link、router-view两种组件，均为Vue在源码中设置的全局组件。路由器对象底层实现的三大步骤即（1）监视地址栏变化；（2）查找当期路径对应的页面组件；（3）将找到的页面组件替换到router-view的位置

### **2.** 配置路由的过程

#### **A：搭载框架**

1.使用npm install安装插件

2.在router/index.js中，使用`vue.use（VueRouter）`使用插件

3.配置路由，创建路由和页面跳转之间的映射关系，并`export default router`导出

4.将router对象传入到Vue实例中,即在Vue实例中挂载创建的路由实例（在main.js中使用`import router from ‘./router/index.js`导入,

```js
import router from './router';
const routers =[
 {
    path: '/',
    name:'Default',
    redirect:'/home',   //请求根目录时，重定向到home页面下
    meta:{
      title:'default'
    }
  }, {
    path: '/home/',
    name:'Home',
    component: App,
    meta:{
      title:'home'
    }
  }
]
export default routers

new Vue({
  router,      //挂载
  store,           
  render: h => h(App),
  beforeCreate() {
    Vue.prototype.$bus = this //安装全局事件总线
  }
```

#### **B：设置映射关系**

例：配置路由

```js
const routers =[
 {
    path: '/',
    name:'Default',
    redirect:'/home',   //请求根目录时，重定向到home页面下
    meta:{
      title:'default'
    }
  }, {
    path: '/home/',
    name:'Home',
    component: App,
    meta:{
      title:'home'
    }
  }
]
```

使用：（router-link相当于一个a标签）

```
<!--      由于controls有子路由，必须在该组件下设置router-view进行子路由占位  -->
        <router-link to="/home/news" >news</router-link>
        <router-link to="/home/about">about</router-link>
```

最后使用<router-view>相当于渲染组件的占位

### 3. vue-router路由模式有几种？

#### 1.Hash



**简介：** hash模式是开发中默认的模式，它的URL带着一个#，例如：http://www.abc.com/#/vue，它的hash值就是#/vue，可以使用`window.location.has`属性读取。

**特点：**hash值会出现在URL里面，但是不会出现在HTTP请求中，对后端完全没有影响。所以改变hash值，不会重新加载页面，但是每一次改变`#`后的部分，都会在浏览器的访问历史中增加一个记录。这种模式的浏览器支持度很好，低版本的IE浏览器也支持这种模式。hash路由被称为是前端路由，已经成为SPA（单页面应用）的标配。

**原理：** hash模式的主要原理就是onhashchange()事件：

```js
window.onhashchange = function(event){
	console.log(event.oldURL, event.newURL);
	let hash = location.hash.slice(1);
}
```

使用onhashchange()事件的好处就是，在页面的hash值发生变化时，无需向后端发起请求，window就可以监听事件的改变，并按规则加载相应的代码。除此之外，**hash值变化对应的URL都会被浏览器记录下来，这样浏览器就能实现页面的前进和后退**。虽然是没有请求后端服务器，但是页面的hash值和对应的URL关联起来了。

#### 2.History

 **简介：**history模式的URL中没有`#`，它使用的是**传统的路由分发模式**，即用户在输入一个URL时，服务器会接收这个请求，并解析这个URL，然后做出相应的逻辑处理。

**特点：** 当使用history模式时，URL就像这样：http://abc.com/user/id。相比hash模式更加好看。但是，history模式需要后台配置支持。如果后台没有正确配置，访问时会返回404。

**API：** history api可以分为两大部分，切换历史状态和修改历史状态：

- 修改历史状态：包括了 HTML5 History Interface 中新增的 pushState() 和 replaceState() 方法，这两个方法**应用于浏览器的历史记录栈**，提供了对历史记录进行修改的功能。只是当他们进行修改时，虽然修改了url，但浏览器不会立即向后端发送请求。如果要做到改变url但又不刷新页面的效果，就需要前端用上这两个API。
- 切换历史状态： 包括forward()、back()、go()三个方法，对应浏览器的前进，后退，跳转操作。
  虽然history模式丢弃了丑陋的#。但是，它也有自己的缺点，就是在刷新页面的时候，如果没有相应的路由或资源，就会刷出404来。

#### 3.Abstract

abstract: 支持所有 JavaScript 运行环境，如 Node.js 服务器端。如果发现没有浏览器的 API，路由会自动强制进入这个模式.

#### 4.Hash和history的对比

- hash模式：通过`#号`后面的内容的更改，触发`onhashchange`事件，实现路由切换。所以Hash只能设置与当前URL同文档的URL。history模式：通过`pushState`和`replaceState`切换url，实现路由切换，需要后端配合。但是history可以设置新的URL可以是与当期URL同源的任意URL
- pushState() 设置的新 URL 可以与当前 URL 一模一样，这样也会把记录添加到栈中；而 hash 设置的新值必须与原来不一样才会触发动作将记录添加到栈中；
- hash模式下，**仅hash符号`#`之前的url会被包含在请求中**，后端如果没有做到对路由的全覆盖，也不会返回404错误；history模式下，前端的url必须和实际向后端发起请求的url一致，如果没有对用的路由处理，将返回404错误。
- pushState() 通过 stateObject 参数可以添加任意类型的数据到记录中；而 hash 只可添加短字符串；

### 4.怎么定义vue-router 的动态路由? 怎么获取传过来的值？

答：在router目录下的index.js文件中，对path属性加上/:id。 使用router对象的params.id。（“：to”：写成对象形式，v-bind）

```js

//在APP.vue中
<router-link :to="'/user/'+userId" replace tag="div&span等">用户</router-link>    //router-link默认渲染一个a标签，可以通过tag控制
computed(){
	userId(){
		return this.$route.params.user    //获取当前活跃的路由
	}
}

//在index.js
{
   path: '/user/:userid',  //配置路由接收的形参
   component: User,
},
  
```

### 5.vue-router实现路由懒加载（ 动态加载路由 ）

**1.背景**：当打包构建应用的时候。Js包会变得非常大（路由中通常会定义很多不同的界面，这些页面最终是放在一个js文件中的，导致这个页面非常大），影响页面加载，甚至用户电脑还会出现短暂的空白

**2.作用**：将路由对应的组件打包成一个个的js代码块，只有当这个路由被访问到时，才加载对应的组件

**3.方式**：

- 第一种：Vue异步组件技术,异步加载. Vue-router配置路由, 使用Vue的异步组件技术, 可以实现按需加载 .但是,这种情况下一个组件生成一个js文件。

- 第二种：路由懒加载(使用import，推荐)

  ```js
  const bundle = ()=> import('../components/bundle.vue')   //路由懒加载的方式
  import controls from "@/components/controls";       //非路由懒加载的方式
  
  const routes=[{
      path: '/',
      name:'Default',
      redirect:'/home'   //请求根目录时，重定向到home页面下
      }, {
          path: '/clear_all',
          name:'Bundle',
          component: bundle   //路由懒加载的方式  等同于component:()=>import('../components/bundle.vue')
      },
      {
          path: '/login/:user',
          name: 'login',
          component: controls    //非路由懒加载的方式
      }
  ]
  ```

- 第三种：webpack提供的require.ensure()，vue-router配置路由，使用webpack的require. ensure技术，也可以实现按需加载。这种情况下，多个路由指定相同的chunkName，会合并打包成一个js文件。

- 第四种：AMD写法

  ```
  const About = resolve => require(['../components/About.vue'],resolve)
  ```

### 6.$route和 $router 的区别

答：$router是在`/router/index.js`文件中定义的VueRouter的实例（**路由器**），在源码中为一个大类，有push、replace、to等方法（script标签中想要导航到不同的URL,使用`$router.push`方法。返回上一个历史history用$router.to(-1)）

`$route`为当前router跳转对象（当前活跃路由）。里面可以获取当前路由的name,path,query,parmas等。

### 7.VUE路由钩子在生命周期函数中的体现

触发进入其他路由：

- 调用要离开的路由守卫 beforeRouteLeave
- 调用全局守卫 beforeEach
- 在重用的组件中调用 beforeRouteUpdate
- 调用路由独享守卫：beforeEnter
- 解析异步路由组件
- 在将要进入的路由中国 beforeRouteEnter
- 调用全局解析守卫 BeforeResolve
- 导航确认
- 调用全局后置钩子  afterEach
- 触发DOM更新 mounted
- 执行beforeRouteEnter守卫中传给next的回调函数

#### 7.1.路由全局导航守卫（拦截）

**背景**：以一个需求为例：当窗口的title需要跟随路由的变化而变化时，可以使用生命周期函数，在开始创建组件时，就设置title，即

```js
export default{
	name:"controls",
	created(){
		document.title = 'controls'
	}
}
```

这种方法需要跳转不同的路由组件，并设置每个组件的created函数，工作量大

**常见的场景：**登录权限验证，当用户满足条件时，才让其进入导航，否则就取消跳转，并跳到登录页面让其登录。

**目的：**导航守卫主要用于监听路由的进入和离开，vue-router提供了beforeEach和afterEach的钩子函数（属于全局守卫），会在路由即将改变前和改变后触发

此外导航守卫还有还有全局解析守卫(router.beforeResolve)、路由独享守卫，组件内的守卫等等

- 全局前置/钩子：beforeEach、beforeResolve、afterEach
- 路由独享的守卫：beforeEnter
- 组件内的守卫：beforeRouteEnter、beforeRouteUpdate、beforeRouteLeave

**使用场景：**

- beforeEach（判断是否登录了，没登录就跳转到登录页）

- afterEach （跳转之后滚动条回到顶部）

- beforeRouteEnter∶ 进入组件前触发，beforeRouteEnter组件内还访问不到this，因为该守卫执行前组件实例还没有被创建，需要传一个回调给 next来访问

  ```js
  beforeRouteEnter(to, from, next) {      
      next(target => {        
          if (from.path == '/classProcess') {          
              target.isFromProcess = true        
          }      
      })    
  }
  ```

- beforeRouteUpdate∶ 当前地址改变并且改组件被复用时触发，举例来说，带有动态参数的路径foo/∶id，在 /foo/1 和 /foo/2 之间跳转的时候，由于会渲染同样的foa组件，这个钩子在这种情况下就会被调用

- beforeRouteLeave∶ 离开组件被调用

```js
router.beforeEach((to,from,next) => {   //全局导航守卫
    //从from跳转到to
    document.title = to.matched[0].meta.title  //to参数的类型是route
    next()   //回调函数，必须调用，也可使用next跳转到其他地址
})

//route的设置
{
        path:'/show_message',
        name:'Sankey',
        component:sankey,
        meta:{
            title:'sankey'
        },
        beforeEnter:(to,from,next) =>{   //路由独享守卫
            console.log('即将进入登录界面')
        }
    },{
        path: '/clear_all',
        name:'Bundle',
        component: bundle,
        meta:{
            title:'bundle'
        }
}
```

#### 7.2 路由独享守卫

如果你不想全局配置守卫的话，你可以为某些路由单独配置守卫：

```js
    const router = new VueRouter({
      routes: [
        {
          path: '/foo',
          component: Foo,
          beforeEnter: (to, from, next) => { 
            // 参数用法什么的都一样,调用顺序在全局前置守卫后面，所以不会被全局守卫覆盖
            // ...
          }
        }
      ]
    })
```

在离开某个模块时，弹出“确认要离开吗”提示框

1. beforeRouteEnter 进入路由前
2. beforeRouteUpdate (2.2) 路由复用同一个组件时
3. beforeRouteLeave 离开当前路由时



### 8.路由的嵌套（子路由）

在父级路由中定义children

```js
  {
        path: '/login/:user',
        name: 'login',
        component: controls,    //非路由懒加载的方式， 由于controls有子路由，必须在该组件下设置router-view
        children:[
            {
                path:'/',
                redirect:'news'  // 默认下显示news
            },
            {
                path:'news',
                component:compare
            },{
                path:'about',
                compent:sankey
            }
        ]
    }

//controls组件中添加如下内容：
 <router-link to="/home/news" >news</router-link>
 <router-link to="/home/about">about</router-link>
 <router-view></router-view>   //router-view一定要出现在子路由对应的组件中
```

### 9.路由的参数传递

**方法一：params的方式**

配置路由格式：/router/:id

传递：使用to方法进行拼接

`<router-link :to=”’/user’+ userid”></>`在computed中动态获取userid进行拼接,传递后形成的路径：`/user/123`

使用：`{{ $route.params.userid }}`

**方法二：query类型(大量数据时适用，传入对象)**

配置路由方式：/router（普通配置），对象中使用query的key作为传递方式，传递后形成的路径`/router?id=123,/router?id=abc`

传递方式一：使用v-bind绑定to属性，使用活跃路由中的query参数获得数据

```js
// App.vue中,跳转到/record路由下，并传递query中的内容
  <router-link :to="{ path: '/record', query:{ name:'why', age:'24', sex:'lady' }}">record</router-link>

//record路由对应的组件中，直接使用$route.query调用
    <h3> { $route.query } </h3>
    <h3> { $route.query.name } </h3>

```

传递方式二：使用methods中的函数传递

```js
//App.vue中
<button @click ='quert_data' ></button>

//methods中
query_data(){
      this.$router.push( {   //必须使用路由器跳转，因为涉及到路由之间的跳转
        path:'/clear_all',
        query:{
          text:"这是通过methods中的函数传递的路由参数数据"
        }
      } )
}

// 路由clear_all对应的组件中
    <h3> { $route.query } </h3>           
//注意：当其他路由活跃且也含有query属性时，会存在显示其他的路由内容
```

**params和query的区别**：

1.query传参，刷新页面不会丢失参数。但是params是保存在内存中的，刷新页面会丢失。
2.使用query传参的话，会在浏览器的url栏看到传的参数类似于get请求，如：http://localhost:8080/info?id=123
而使用params传参的话则不会地址栏看到参数，类似于post请求，这样地址栏会更加美观，如果需要在地址栏显示参数，可在路由声明中path里加上参数（冒号加参数名称）比如 /info/:id, 传参的时候，参数名要跟路由后面设置的参数名对应。query没有这种限制，直接在跳转里面用即可

```
params形成的path：/router/123
query形成的path:  /router1?id=123
```

3.只要在路由声明中添加name属性，query传参可用path也可用name，但是params传参的话，只允许使用name。

4.params是路由的一部分,必须要有。params一旦设置在路由，params就是路由的一部分，如果这个路由有params传参，但是在跳转的时候没有传这个参数，会导致跳转失败或者页面会没有内容。

query是拼接在url后面的参数，没有也没关系。

### 10. 谈谈你对 keep-alive 的了解？

**1. 定义:**keep-alive是 Vue 内置的一个虚拟组件，可以使被包含的组件保留状态，避免重新渲染。一般结合路由和动态组件一起使用，用于缓存组件。常用的两个属性 include、exclude、max，允许组件有条件的进行缓存（提供 include 和 exclude 属性，两者都支持字符串或正则表达式。include表示只有名称匹配的组件会被缓存，exclude表示任何名称匹配的组件都不会被缓存 ，其中 exclude 的优先级比 include高；max 定义最大缓存数量，超过max，使用 LRU 算法，选择最近最久未使用的组件予以淘汰）。**某个组件在路由跳转后不被销毁常驻内存，故，该组件的data也得以保存**

**2.注意事项:**

- keep-alive是虚拟组件，不会生成任何dom
- keep-alive不能同时渲染多个组件，会被忽略（因为源码中 vnode 属性默认只取第一个子组件 var vnode = getFirstComponentChild(slot); ）
- keep-alive 里包裹组件的子组件们都会触发activated和deactivate钩子（2.2.0+）版本后

**3.使用场景:**需要来回切换的业务场景，（例如tab切换或者路由切换），但是数据更新不是很频繁的页面。为用户保存状态，避免每次切换都重新拉数据进行渲染。可以通过activated钩子来触发部分刷新。

**4.使用方式：**两个生命周期：activated/deactivated，用来得知当前组件是否处理活跃状态（对应两个钩子函数 activated 和 deactivated ，当组件被激活时，触发钩子函数 activated，当组件被移除时，触发钩子函数 deactivated。）例：router-view为一个全局组件，如果被包含在keep-alive中，所有路径匹配到的视图组件都会被sdsd缓存

在route设置时使用meta来判定是否缓存，并使用v-if判断

```json
//App.vue中
<keep-alive>
    <router-view v-if="$route.meta.keepAlive" />    //当正在跳转的组件的$route.meta.keepAlive为true时，就将该组件加入缓存，否则不加入缓存。
</keep-alive>
    <router-view v-if="!$route.meta.keepAlive" />

//router中
{
 path:'/',
 name:'home',
 components:Home,
 meta:{
     title:'Home'
  	 keepAlive:true //需要被缓存的组件
 },
 // 也可以在路由守卫中设置keep-alive
 beforeRouteLeave(to,from,next){
    to.meta.keepAlive = true;
    next();
  }
```

### 11.操作Cookie、localStorage、sessionStorage

#### 1.Cookie

```js
//---------------------------存值------------------------------------------
document.cookie = "userId=nick123"

//---------------------------获取------------------------------------------
const cookies = document.cookie
//使用正则表达式匹配cookie
function getCookieValue(name) {
  let result = document.cookie.match("(^|[^;]+)\\s*" + name + "\\s*=\\s*([^;]+)")
  return result ? result.pop() : ""
}
```

#### 2.LocalStorage

localStorage相当于window对象下面的一个属性，所以有[]和.调用，但也具有自身的setItem，getItem方法

 ```js
//-----------------------存值---------------------------------------
// 自身方法
localStorage.setItem("name","bonly");
// []方法
localStorage["name"]="bonly";
// .方法
localStorage.name="bonly";

//---------------------取值-----------------------------------------
// 自身方法
localStorage.getItem("name");
// []方法
localStorage["name"];
// .方法
localStorage.name;

//---------------------移除-------------------------------------------
// 自身方法
localStorage.removeItem("name");
// []方法
delete localStorage["name"];
// .方法
delete localStorage.name

//----------------------取值------------------------------------------
// 通过自身的key
for (var i=0;i<localStorage.length;i++) {
console.log(localStorage.key(i));
}
// 通过for in 循环获取
for(var key in localStorage){
console.log(key);
}

localStorage.hasOwnProperty("name")  // 如果存在的话返回true，不存在返回false
 ```

#### 3.SessionStorage

```js
var name='sessionData';
var num=120;
sessionStorage.setItem(name,num);//存储数据
sessionStorage.setItem('value2',119);
let dataAll=sessionStorage.valueOf();//获取全部数据
console.log(dataAll,'获取全部数据');
var dataSession=sessionStorage.getItem(name);//获取指定键名数据
var dataSession2=sessionStorage.sessionData;//sessionStorage是js对象，也可以使用key的方式来获取值
 console.log(dataSession,dataSession2,'获取指定键名数据');
sessionStorage.removeItem(name); //删除指定键名数据
  console.log(dataAll,'获取全部数据1');
 sessionStorage.clear();//清空缓存数据：localStorage.clear();
  console.log(dataAll,'获取全部数据2');  
```



### 12.路由的hash模式和history模式的区别

>hash 模式和 history 模式都属于浏览器自身的特性，Vue-Router 只是利用了这两个特性（通过调用浏览器提供的接口）来实现前端路由.

#### 1.Hash模式

**简介：** hash模式是开发中默认的模式，它的URL带着一个#，例如：http://www.abc.com/#/vue，它的hash值就是#/vue。
**特点：**hash值会出现在URL里面，但是不会出现在HTTP请求中，对后端完全没有影响。所以改变hash值，不会重新加载页面。这种模式的浏览器支持度很好，低版本的IE浏览器也支持这种模式。hash路由被称为是前端路由，已经成为SPA（单页面应用）的标配。
**原理：** 当hash变化是，触发onhashchange()事件, 这让**hash值变化对应的URL都会被浏览器记录下来**，这样浏览器就能实现页面的前进和后退。虽然是没有请求后端服务器，但是**页面的hash值和对应的URL关联**起来了。使用`window.location.hash`属性及窗口的`onhashchange`事件，可以实现监听浏览器地址`hash`值变化，执行相应的`js`切换网页。

**前进后退：**hash模式会创建hashHistory对象，在访问不同的路由时，会发生两件事：

- `HashHistory.push()`将新的路由添加到浏览器访问历史的栈顶，`HashHistory.replace`替换当前栈顶的路由

```js
window.onhashchange = function(event){
	console.log(event.oldURL, event.newURL);
	let hash = location.hash.slice(1);
}
```

#### 2.History模式

**简介：** history模式的URL中没有#，它使用的是传统的路由分发模式，即用户在输入一个URL时，服务器会接收这个请求，并解析这个URL，然后做出相应的逻辑处理。
**特点：** 当使用history模式时，URL就像这样：http://abc.com/user/id。相比hash模式更加好看。但是，history模式需要后台配置支持。如果后台没有正确配置，访问时会返回404。
**前进后退：** history `api`可以分为两大部分，切换历史状态和修改历史状态：

- 修改历史状态：`pushState()`可以改变url地址且不会发送请求,`replaceState()`可以读取历史记录栈,还可以对浏览器记录进行修改

- 切换历史状态： 包括forward()、back()、go()三个方法，对应浏览器的前进，后退，跳转操作。
  
  ```
  history.go(-2);//后退两次
  history.go(2);//前进两次
  history.back(); //后退
  hsitory.forward(); //前进
  ```
  
  虽然history模式丢弃了丑陋的#。但是，它也有自己的缺点，就是**在刷新页面的时候，如果没有相应的路由或资源，就会刷出404**来。

```js
const router = new VueRouter({
  mode: 'history',
  routes: [...]
})
```

#### 3.两种模式比较

- history和hash都是利用浏览器的两种特性实现前端路由，history是利用浏览历史记录栈的API实现，hash是监听location对象hash值变化事件来实现
- history修改的url可以是同域的任意url，hash是同文档的url
- hash模式下，仅hash符号之前的url会被包含在请求中，后端如果没有做到对路由的全覆盖，也不会返回404错误；history模式下，前端的url必须和实际向后端发起请求的url一致，如果没有对用的路由处理，将返回404错误，所以history往往需要后端的支持，hash因为是同文档的url，即使后端没有覆盖的路由，也不会返回404
- hash模式下，如果把url作为参数传后端，那么后端会直接从’#‘号截断，只处理’#'号前的url，因此会存在**#后的参数内容**丢失的问题，

调用 history.pushState() 相比于直接修改 hash，存在以下优势:

- pushState() 设置的新 URL 可以是与当前 URL 同源的任意 URL；而 hash 只可修改 # 后面的部分，因此只能设置与当前 URL 同文档的 URL；
- pushState() 设置的新 URL 可以与当前 URL 一模一样，这样也会把记录添加到栈中；而 hash 设置的新值必须与原来不一样才会触发动作将记录添加到栈中
- pushState() 通过 stateObject 参数可以添加任意类型的数据到记录中；而 hash 只可添加短字符串；
- pushState() 可额外设置 title 属性供后续使用。

小白回答：hash模式url带#号，history模式不带#号。

大牛回答：hash模式url里面永远带着#号，我们在开发当中默认使用这个模式。那么什么时候要用history模式呢？如果用户考虑url的规范那么就需要使用history模式，因为history模式没有#号，是个正常的url适合推广宣传。比如在开发app的时候有分享页面，那么这个分享出去的页面就是用vue或是react做的，咱们把这个页面分享到第三方的app里，**有的app里面url是不允许带有#号的，所以要将#号去除那么就要使用history模式**，但是使用history模式还有一个问题就是，在访问二级页面的时候，做刷新操作，会出现404错误，那么就需要和后端人配合让他配置一下apache或是nginx的url重定向，重定向到你的首页路由上就ok啦。

#### 4.刷新后参数的存在问题

**结论**：hash模式下，刷新参数不会丢失； history不做配置的话刷新后参数会丢失

**原因**：hash虽然会改变URL，但是其hash值并不会包含在HTTP请求中，hash值被用于指导浏览器动作，并不影响服务端，因此改变hash并没有改变url，页面还是之前的路径，nginx不会拦截。在history模式下，参数会被一同解析，但是并没有目的网址，所以会刷出404错误，此时nginx会对其进行重定向，恢复之前的路由，所以丢失了参数。

#### 5.如何获取页面的hash变化

**1）监听$route的变化**

```js
// 监听,当路由发生变化的时候执行
watch: {
  $route: {
    handler: function(val, oldVal){
      console.log(val);
    },
    // 深度观察监听
    deep: true
  }
},
```

**2）window.location.hash读取#值**
window.location.hash 的值可读可写，读取来判断状态是否改变，写入时可以在不重载网页的前提下，添加一条历史访问记录。

**12.Vue-router跳转和location.href有什么区别**

答：使用location.href='/url'来跳转，简单方便，但是刷新了页面；

使用history.pushState('/url')，无刷新页面，静态跳转；

引进router，然后使用router.push('/url')来跳转，使用了diff算法，实现了按需加载，减少了dom的消耗。

其实使用router跳转和使用history.pushState ()没什么差别的，因为vue-router就是用了history.pushState()，尤其是在history模式下。

### 13.对前端路由的理解

Vue中路由跳转分为**编程式**和**声明式**

声明式：

使用router-link组件来导航，通过传入to属性指定连接，当需要在一个页面中嵌套子路由，并且页面不跳转的时候使用这种方式

编程式：使用vue-router

对于vue这类渐进式前端开发框架，为了构建 SPA（单页面应用），需要引入前端路由系统，这也就是 Vue-Router 存在的意义。前端路由的核心，就在于 —— 改变视图的同时不会向后端发出请求。

> 在前端技术早期，一个 url 对应一个页面，如果要从 A 页面切换到 B 页面，那么必然伴随着页面的刷新。这个体验并不好，不过在最初也是无奈之举——用户只有在刷新页面的情况下，才可以重新去请求数据。
>
> 后来，改变发生了——**Ajax 出现了，它允许人们在不刷新页面的情况下发起请求**；与之共生的，还有“**不刷新页面即可更新页面内容**”这种需求。在这样的背景下，出现了 **SPA（单页面应用）**。对应的，有多页面应用模式
>
> SPA极大地提升了用户体验，它**允许页面在不刷新的情况下更新页面内容，使内容的切换更加流畅**。但是在 SPA 诞生之初，人们并没有考虑到“定位”这个问题——在内容切换前后，页面的 URL 都是一样的，这就带来了两个问题：
>
> 1. SPA 其实并不知道当前的页面“进展到了哪一步”。可能在一个站点下经过了反复的“前进”才终于唤出了某一块内容，但是此时只要刷新一下页面，一切就会被清零，必须重复之前的操作、才可以重新对内容进行定位——**SPA 并不会“记住”你的操作**。
> 2. 由于有且仅有一个 URL 给页面做映射，这对 SEO 也不够友好，搜索引擎无法收集全面的信息
>
> 为了解决这个问题，前端路由出现了。
>
> 前端路由可以帮助我们在仅有一个页面的情况下，“记住”用户当前走到了哪一步——为 SPA 中的各个视图匹配一个唯一标识。这意味着用户前进、后退触发的新内容，都会映射到不同的 URL 上去。此时即便他刷新页面，因为当前的 URL 可以标识出他所处的位置，因此内容也不会丢失。
>
> 那么如何实现这个目的呢？首先要解决两个问题：
>
> 1. 当用户刷新页面时，浏览器会默认根据当前 URL 对资源进行重新定位（发送请求）。这个动作对 SPA 是不必要的，因为我们的 SPA 作为单页面，无论如何也只会有一个资源与之对应。此时若走正常的请求-刷新流程，反而会使用户的前进后退操作无法被记录。
> 2. 单页面应用对服务端来说，就是一个URL、一套资源，那么如何做到用“不同的URL”来映射不同的视图内容呢？
>
> 从这两个问题来看，服务端已经完全救不了这个场景了。所以要靠咱们前端自力更生，不然怎么叫“前端路由”呢？作为前端，可以提供这样的解决思路：
>
> 1. 拦截用户的刷新操作，避免服务端盲目响应、返回不符合预期的资源内容。把刷新这个动作完全放到前端逻辑里消化掉。
> 2. 感知 URL 的变化。这里不是说要改造 URL、凭空制造出 N 个 URL 来。而是说 URL 还是那个 URL，只不过我们可以给它做一些微小的处理——这些处理并不会影响 URL 本身的性质，不会影响服务器对它的识别，只有我们前端感知的到。一旦我们感知到了，我们就根据这些变化、用 JS 去给它生成不同的内容。



|               /                | 多页面应用模式MPA                                  | 单页面应用模式SPA                                            |
| :----------------------------: | -------------------------------------------------- | ------------------------------------------------------------ |
|          **应用构成**          | 由多个完整页面构成                                 | 一个外壳页面和多个页面片段构成                               |
|          **跳转方式**          | 页面之间的跳转是从一个页面到另一个页面             | 一个页面片段删除或隐藏，加载另一个页面片段并显示。片段间的模拟跳转，没有开壳页面 |
| **跳转后公共资源是否重新加载** | 是                                                 | 否                                                           |
|          **URL模式**           | `http://xxx/page1.html`和`http://xxx/page2.html`   | `http://xxx/shell.html#page1`和`http://xxx/shell.html#page2` |
|          **用户体验**          | 页面间切换加载慢，不流畅，用户体验差，尤其在移动端 | 页面片段间切换快，用户体验好，包括移动设备                   |
|      **能否实现转场动画**      | 否                                                 | 容易实现（手机APP动效）                                      |
|       **页面间传递数据**       | 依赖`URL`、`cookie`或者`localstorage`，实现麻烦    | 页面传递数据容易（`Vuex`或`Vue`中的父子组件通讯`props`对象） |
|    **搜索引擎优化（SEO）**     | 可以直接做                                         | 需要单独方案（SSR）                                          |
|       **特别适用的范围**       | 需要对搜索引擎友好的网站                           | 对体验要求高，特别是移动应用                                 |
|          **开发难度**          | 较低，框架选择容易                                 | 较高，需要专门的框架来降低这种模式的开发难度                 |

### 14.通过路由实现权限控制

**思路**：

- 直接将路由表保存在服务器端，通过登录返回对应的路由表
- 设置路由守卫，通过用户的权限将对应的路由添加到路由表中





## 七、Promise相关

### 1.异步操作补充

同步（sync）指的是一次只能完成一件任务。如果有多个任务，就必须排队，前面一个任务完成，再执行后面一个任务，以此类推。异步（async）指的是每一个任务有一个或多个回调函数（callback），前一个任务结束后，不是执行后一个任务，而是执行回调函数，后一个任务则是不等前一个任务结束就执行，所以程序的执行顺序与任务的排列顺序是不一致的、异步的。

### 2. promise的定义

promise是异步编程的一种解决方案，对异步操作进行封装。其中，异步操作主要出现在网络请求当中，当出现复杂的网络请求时，就会出现回调地狱

基本使用如下：

```js
//链式编程

//参数->函数,resolve，reject本身也是函数
new Promise((resolve,reject)=>{
    //第一次网络请求代码
    setTimeout((data)=>{
        resolve()          //一旦resolve，就会调用.then函数
        				
    }，1000)
}).then(()=>{            //下一次的网络请求都在上一个函数的then方法中
    console.log('aaaaa')
    console.log('aaaaa')
    console.log('aaaaa')
    return new Promise((resolve,reject)=>{
         //第二次网络请求代码
    	setTimeout(()=>{
        	resolve()          //一旦resolve，就会调用.then函数
    	}，1000)
    }).then(()=>{
        console.log('bbbb')
    	console.log('bbbbbb')
    	console.log('bbbbbb')
        return new Promise((resolve,reject)=>{
         //第三次网络请求代码
    	setTimeout(()=>{
        	resolve()           //失败时调用reject,调用catch函数
    	}，1000)
    }).catch((err)=>{
        console.log(err)
    	
    })
})
```

### 3.Promise的三种状态

pending:等待状态，比如正在进行网络请求，或定时器未到时间

fulfill：满足状态，当主动回调resolve时，就处于该状态，并会回调.then（）

reject：拒绝状态，当主动回调reject时，处于该状态，并会回调.catch()

### 4.Promise的all方法

promise.all()该方法用于将多个Promise实例，包装成一个新的Promise实例

var p = Promise.all([p1,p2,p3]);
（1）只有p1、p2、p3的状态都变成fulfilled，p的状态才会变成fulfilled，此时p1、p2、p3的返回值组成一个数组，传递给p的回调函数。
（2）只要p1、p2、p3之中有一个被rejected，p的状态就变成rejected，此时第一个被reject的实例的返回值，会传递给p的回调函数。

PS:promise.all()成功时，在then（result）中result是个数组

>##### 实战面试(PDD)：
>
>1.问题描述
>
>- 给你一个`userIdList`,用户id列表.
>- 只有一个接口，根据`userId`获取单个用户`userInfo`信息。
>- 如何渲染出多个用户信息列表`userInfoList`，没有用户信息列表的接口
>- 接口：`https://api.agify.io/?name=lucy`，`['nice','david','tony']`这三个人对应的年龄应该是`[19,63,54]`
>
>2.实现
>
>Promise：
>
>```js
>let getUserInfo =[]
>const nameList = ['nice','david','tony']
>for(let i of nameList){
>    new Promise(resolve,rej ect)=>{
>         axios.get(
>    	`https://api.agify.io/?name=${i}`
>    ).then(res=>{
>        resolve(res)
>    },err=>{
>        reject(err)
>    })
>    }.then(res=>{
>        this.getUserInfo.push(res.data.age)  //请求体中数据全部都在data中，所以必须有data前缀。此时为最终值，但是没有按照nameList列表顺序
>    })
>}
>
>//如果将age按照顺序排序，则使用promise.all
>for(let i of nameList){
>    getUserInfo.push(
>    	  new Promise(resolve,reject)=>{
>         axios.get(
>    	`https://api.agify.io/?name=${i}`
>            ).then(res=>{
>                resolve(res)
>            },err=>{
>                reject(err)
>            })
>            }.then(res=>{
>                this.getUserInfo.push(res.data.age)  
>    //请求体中数据全部都在data中，所以必须有data前缀。此时为最终值，但是没有按照nameList列表顺序
>            })
>    )
>}
>Promise.all(getUserInfo).then(res)=>{   //此时getUserInfo按照for循环，所有promise的结果一定是有序的
>    for(let i of res){
>        this.getUserInfor.push(i.data.age)
>    }
>}
>```
>
>Async/await
>
>```js
>async getInfo(){
>    const nameList = ['nice','david','tony']
>    for(let i of nameList){
>        let value = await axios.get(
>        `https://api.agify.io/?name=${i}`
>        )
>        this.getUserInfo.push(val.data.age)  //age和姓名顺序能够保持一致
>    }
>}
>```
>
>

## 八、VUE 3.0

### 1. VUE 3.0有什么更新

#### **（1）监测机制的改变**

- 3.0 将带来基于代理 Proxy的 observer 实现，提供全语言覆盖的反应性跟踪。
- 消除了 Vue 2 当中基于 Object.defineProperty 的实现所存在的很多限制（无法监听到数组等）
- Vue2.x版本中的双向绑定不能检测到下标的变化，proxy可以劫持整个对象，并返回一个新对象

#### **（2）只能监测属性，不能监测对象**

- 检测属性的添加和删除；
- 检测数组索引和长度的变更；
- 支持 Map、Set、WeakMap 和 WeakSet。

#### **（3）作用域插槽**

- 作用域插槽：2.x 的机制导致作用域插槽变了，父组件会重新渲染，而 3.0 把作用域插槽改成了函数的方式，这样只会影响子组件的重新渲染，提升了渲染的性能。
- 同时，对于 render 函数的方面，vue3.0 也会进行一系列更改来方便习惯直接使用 api 来生成 vdom 。

#### **（4）结构目录改变**

- vue-cli3移除了配置文件目录（config），跨域需要配置域名时，从config/index.js 挪到了vue.config.js中，配置方法不变 
- vue-cli3中移除了static静态文件夹，新增了public文件夹
- 在src文件中新增了views文件夹，用于分类视图组件和公共组件

#### **（5）生命周期函数变化**

在 vue 3.0 中，生命周期是从 vue 中导出的，我们需要用到哪些，就导出哪些。这样的好处是，在实际开发中，我们用不到所有的生命周期函数，通过导出的方式，可以减少项目的体积。

**注**：setup生命周期函数在外侧，其余所有的生命周期函数都是在setup里面直接书写

| 2.0 周期名称  | 3.0 周期名称    | 说明                          |
| ------------- | --------------- | ----------------------------- |
| beforeCreate  | setup           | 组件创建之前                  |
| created       | setup           | 组件创建完成                  |
| beforeMount   | onBeforeMount   | 组件挂载之前                  |
| mounted       | onMounted       | 组件挂载完成                  |
| beforeUpdate  | onBeforeUpdate  | 数据更新，虚拟 DOM 打补丁之前 |
| updated       | onUpdated       | 数据更新，虚拟 DOM 渲染完成   |
| beforeDestroy | onBeforeUnmount | 组件销毁之前                  |
| destroyed     | onUnmounted     | 组件销毁后                    |

```js
import {      //仅导入使用的生命周期函数
onBeforeMount,
onMounted,
onBeforeUpdate,
onUpdated,
onBeforeUnmount,
onUnmounted,
ref
} from 'vue'

export default {
setup () {     // setup 函数，就相当于 vue 2.0 中的 created。其余所有的生命周期函数都写在setup函数中
const count = ref(0)

onBeforeMount (() => {
count.value++
console.log('onBeforeMount', count.value)
})
    
onMounted (() => {
count.value++
console.log('onMounted', count.value)
})
 
// 注意，onBeforeUpdate 和 onUpdated 里面不要修改值，会死循环的哦！一直修改，一直刷新
onBeforeUpdate (() => {
console.log('onBeforeUpdate', count.value)
})
 
onUpdated (() => {
console.log('onUpdated', count.value)
})
 
onBeforeUnmount (() => {
count.value++
console.log('onBeforeUnmount', count.value)
})
 
onUnmounted (() => {
count.value++
console.log('onUnmounted', count.value) 
})

```

#### （6）对文件的引用上

- Vue2.x中new出的实例对象，所有的东西都在这个vue对象上，这样其实无论你用到还是没用到，都会跑一变。
- vue3.0中可以用ES module imports按需引入，如：keep-alive内置组件、v-model指令，等等

#### （7）语法方面

1.`v-model`语法糖废弃，改用 `modelValue`

```xml
<input v-model="value" />
<input modelValue="value" />
```

2.弃用全局API `new Vue` ,使用 `createApp`

```javascript
const app = Vue.createApp({})
```

3.不能再使用`Vue.nextTick`/`this.$nextTick`，Vue3中你可以用：

```js
import { nextTick } from 'vue'
nextTick(() => {
  // something
})
```

4.手动挂载根节点

```js
//main.js
 
import { createApp } from 'vue'
import App from './App.vue'

createApp(App).mount('#app')
```

5.监听数组变化需要使用`deep`属性，否则只能监听到整个数组被替换

6.弃用`$children`，访问子组件可以使用`$ref`

7.移除事件API，`$on`,`$once`,`$off`不再使用。`EventBus`方法也不再使用。

8.Vue的2.0 版本中，使用 Vue.set 来给对象新增一个属性时，这个对象的所有 watcher 都会重新运行；3.x 版本中，只有依赖那个属性的 watcher 才会重新运行

### 2. Object.definedProperty和proxy的区别

二者都可以实现数据劫持，实现MVVM中的双向数据绑定。

Object.defineProperty()Vue 在实例初始化时**遍历 data 中的所有属性**，并使用把这些属性全部转为 getter/setter。这样当追踪数据发生变化时，setter 会被自动调用。 它的问题主要有三个：

- 不能监听数组的变化（VUE缓存了array的原型链，重写了原型，触发push, pop, shift, unshift,splice, sort, reverse方法时会observe数据，让Object.definedProperty可以监听到这些数组，其他的数组方法不能监听到），一般使用Vue.$set或vue.$delect触发响应式
- 必须遍历对象的每个属性
- 必须深层遍历嵌套的对象

proxy的特性

- 因为proxy使用ES6，所以其兼容性不如 Object.defineProperty()
- Proxy直接代理整个对象而非对象属性，只需做一层代理就可以监听同级结构下的所有属性变化，包括新增属性和删除属性，重要的是包括数组的变化
- 在实现深度监听的时候，只有在data对象的属性被访问的时候，才去对这个属性做监听处理，而不是一次性递归所有的。

- 支持Map，set，weakmap和weakSet

## 九、其他

### 1.Vue和React的异同

#### 1.相同点

- 都将注意力集中保持在核心库，而将其他功能如路由和全局状态管理交给相关的库；
- 都使用了Virtual DOM（虚拟DOM）提高重绘性能；
- 都有props的概念，允许组件间的数据传递；
- 都鼓励组件化应用，将应用分拆成一个个功能明确的模块，提高复用性
- 都有自己的构建工具，能让你得到一个根据最佳实践设置的项目模板；

#### 2.不同点

1）数据流
Vue默认支持数据双向绑定，而React一直提倡单向数据流 

2）虚拟DOM
Vue2.x开始引入"Virtual DOM"，消除了和React在这方面的差异，但是在具体的细节还是有各自的特点。 

- Vue宣称可以更快地计算出Virtual DOM的差异，这是由于它在渲染过程中，会跟踪每一个组件的依赖关系，不需要重新渲染整个组件树。
- 对于React而言，每当应用的状态被改变时，全部子组件都会重新渲染。当然，这可以通过 PureComponent/shouldComponentUpdate这个生命周期方法来进行控制，但Vue将此视为默认的优化。

3) 组件化

React与Vue最大的不同是模板的编写。

- Vue鼓励写近似常规HTML的模板。写起来很接近标准 HTML元素，只是多了一些属性。
- React推荐你所有的模板通用JavaScript的语法扩展——JSX书写。

具体来讲：React中render函数是支持闭包特性的，所以import的组件在render中可以直接调用。但是在Vue中，由于模板中使用的数据都必须挂在 this 上进行一次中转，所以 import 一个组件完了之后，还需要在 components 中再声明下。

4）监听数据变化的实现原理不同

- Vue 通过 getter/setter 以及一些函数的劫持，能精确知道数据变化，不需要特别的优化就能达到很好的性能
- React 默认是通过比较引用的方式进行的，如果不优化（PureComponent/shouldComponentUpdate）可能导致大量不必要的vDOM的重新渲染。这是因为 Vue 使用的是可变数据，而React更强调数据的不可变。

5）高阶组件
react可以通过高阶组件（HOC）来扩展，而Vue需要通过mixins来扩展。高阶组件就是高阶函数，而React的组件本身就是纯粹的函数，所以高阶函数对React来说易如反掌。相反Vue.js使用HTML模板创建视图组件，这时模板无法有效的编译，因此Vue不能采用HOC来实现。

6）构建工具
两者都有自己的构建工具：

- React ==> Create React APP
- Vue ==> vue-cli

7）7）跨平台

- React ==> React Native
- Vue ==> Weex

### 2.常用的调试方法

- throw error，扔出错误
- console.log 打印日志
- 用 ChromeVUE的 Devtools 的 debugger 来调试
- 用 webstorm的 debugger 来调试

### 2.你使用Vue框架中踩过最大的坑是什么？怎么解决的？



```markdown
1. Vue 实例的 data 属性，可以在哪些生命周期中获取到？
A. beforeCreate
B. created
C. beforeMount
D. mounted

2. 下列对 Vue 原理的叙述，哪些是正确的？
A. Vue 中的数组变更通知，通过拦截数组操作方法而实现
B. 编译器目标是创建渲染函数，渲染函数执行后将得到 VNode 树
C. 组件内 data 发生变化时会通知其对应 watcher，执行异步更新
D. patching 算法首先进行同层级比较，可能执行的操作是节点的增加、删除和更新

3. 对于 Vue 中响应式数据原理的说法，下列哪项是不正确的？
A. 采用数据劫持方式，即 Object.defineProperty() 劫持 data 中各属性，实现响应式数据
B. 视图中的变化会通过 watcher 更新 data 中的数据
C. 若 data 中某属性多次发生变化，watcher 仅会进入更新队列一次
D. 通过编译过程进行依赖收集

4. 下列说法不正确的是哪项？
A. key 的作用主要是为了高效地更新虚拟 DOM
B. 若指定了组件的 template 选项，render 函数不会执行
C. 使用 vm.$nextTick 可以确保获得 DOM 异步更新的结果
D. 若没有 el 选项，vm.$mount(dom) 可将 Vue 实例挂载于指定元素上

5. 下列关于 Vuex 的描述，不正确的是哪项？
A. Vuex 通过 Vue 实现响应式状态，因此只能用于 Vue
B. Vuex 是一个状态管理模式
C. Vuex 主要用于多视图间状态全局共享与管理
D. 在 Vuex 中改变状态，可以通过 mutations 和 actions

6. 关于 Vue 组件间的参数传递，下列哪项是不正确的？
A. 若子组件给父组件传值，可使用 $emit 方法
B. 祖孙组件之间可以使用 provide 和 inject 方式跨层级相互传值
C. 若子组件使用 $emit('say') 派发事件，父组件可使用 @say 监听
D. 若父组件给子组件传值，子组件可通过 props 接受数据

7. 下列关于 vue-router 的描述，不正确的是哪项？
A. vue-router 的常用模式有 hash 和 history 两种
B. 可通过 addRoutes 方法动态添加路由
C. 可通过 beforeEnter 对单个组件进行路由守卫
D. vue-router 借助 Vue 实现响应式的路由，因此只能用于 Vue

8. 下列说法不正确的是哪项？
A. 可通过 this.$parent 查找当前组件的父组件
B. 可使用 this.$refs 查找命名子组件
C. 可使用 this.$children 按顺序查找当前组件的直接子组件
D. 可使用 $root 查找根组件，并可配合 children 遍历全部组件

9. 下列关于 v-model 的说法，哪项是不正确的？
A. v-model 能实现双向绑定
B. v-model 本质上是语法糖，它负责监听用户的输入事件以更新数据
C. v-model 是内置指令，不能用在自定义组件上
D. 对 input 使用 v-model，实际上是指定其 :value 和 :input

10. 关于 Vue 的生命周期，下列哪项是不正确的？
A. DOM 渲染在 mounted 中就已经完成了
B. Vue 实例从创建到销毁的过程，就是生命周期
C. created 表示完成数据观测、属性和方法的运算和初始化事件，此时 $el 属性还未显示出来
D. 页面首次加载过程中，会依次触发 beforeCreate，created，beforeMount，mounted，beforeUpdate，updated

1. BCD
2. ABCD
3. BD
4. B
5. C // 据出题人勘误称答案应该是 D
6. B
7. C
8. C
9. C
10. D
```

## 十、Vue场景题

### 1. VUE实现权限控制

#### 1. 权限分类

- 后端权限：权限的核心是服务器中的数据变化，后端权限可以控制某个用户是否能够查询数据，是否能够修改数据等操作

  - 后端如何知道该请求是哪个用户发过来的—–状态保持

    ```js
    cookie
    session
    token
    ```

  - 后端的权限设计RBAC（基于角色的权限控制）

    ```markdown
    用户
    角色
    权限
    ```

- 前端权限：
  - 前端权限的控制本质上来说， 就是控制端的**视图层的展示**和前端所发送的**请求**。但是只有前端权限控制没有后端权限控制是万万不可的。 前端权限控制只可以说是达到锦上添花的效果。
  - 前端权限的优点在于：
    - **降低非法操作的可能性**
      不怕赃偷就怕贼惦记， 在页面中展示出一个**就算点击了也最终会失败的按钮**，势必会增加有心者非法操作的可能性（黑客可能会根据按钮的形式和内容作出一些非法操作），前端权限控制就是控制这些按钮的出现与否
    - **尽可能排除不必要清求， 减轻服务器压力**
      没必要的请求， 操作失败的清求， 不具备权限的清求， 应该压根就不需要发送， 请求少了， 自然也会减轻服务器的压力。（这些请求可以直接在前端拦截）
    - **提高用户体验**
      根据用户具备的权限为该用户展现自己权限范围内的内容， 避免在界面上给用户带来困扰， 让用户专注于分内之事

#### 2.前端权限控制思路

##### 2.1 菜单的控制

>在服务器返回的**res**数据中，有两项非常重要：
>
>- 一个是token信息，保存用户的登录状态，
>- rights：该用户具备的权限数据，一级权限就对应一级菜单，二级权限就对应二级菜单

在登录请求中， 会得到权限数据， 当然， 这个需要后端返回数据的支持． 前端根据权限数据， 展示对应的菜单． 点击菜单， 才能查看相关的界面

```js
// 1. 菜单需要根据不同的用户产生不同的内容，一般使用v-for填充内容
v-for = "item" in menulist
//而menulist一般是一个数组，根据权限的数据对数组内容进行填充。而权限数据一般在login.vue中获取，并使用vuex共享状态

//2.在vuex中实现登录状态管理
state:{
    rightList:[]
},
mutations:{
    setRightlist(state,data){
        state.rightList = data
    }
}
//3.在login.vue中调用setrightlist方法，填充
methods:{
    login(){
        this.$store.commit('setRightlist',res.data) //res是后台服务器返回的数据,存储着菜单数据的内容
    }
}

//4.在home.vue中填充侧边栏的内容
import { mapState } from 'vuex'
computed:{
    ...mapState(['rightList'])  //映射vuex中的数据
}
created:{
    this.menulist = this.rightList  //填充菜单栏的数据，如果rightlist中的数据与menulist中的数据不符，也可以在之前进行一些修改操作
}
mthods:{
    logout:{ 
        //登出操作，清空缓存和vuex中的内容，跳转到登录界面
        sessionStorage.clear()
        this.$router.push('/login')
        window.location.reload()
    }
}
```

但是上述数据是存储在vuex中的，如果页面刷新，则vuex初始化，rightlist数据丢失，所以需要数据持久化，将权限数据存储在sessionStorage中，并让其和vuex中的数组保持同步

```js
//在vuex中
state:{
    rightList: JSON.parse(sessionStroage.getItem('rightList') || '[]')  //获取缓存中的数据，并将其转换为数组
},
mutations:{
    setRightlist(state,data){
        state.rightList = data
        sessionStorage.setItem('rightList',JSON.stringify(data))   //rightlist是个数组，将其转化为字符串存储在sessionstorage中
    }
}
```

##### 2.2 界面的控制

有两种情况：

情况1：如果用户没有登录， 手动在地址栏敲入管理界面的地址， 则需要跳转到登录界面；

- 如何判断是否登录：

  ```js
  sessionStorage.setItem('token',res.data.token)
  ```

- 什么时机

  - 路由导航守卫

    ```js
    router.beforEach((to,from,next)=>{
        if(to.path ==='/login'){
            next()
        }else{
            const token = sessionStroge.getItem('token')
            if(!token){
                next('/login')
            }else{
                next()
            }
        }
    })
    ```

  情况2：如果用户已经登录， 如果手动敲入非权限内的地址， 则需要跳转404 界面

- 路由导航守卫：

  路由导航后卫可以在每次路由地址发生变化时，从vuex中取出rightList判断用户将要访问的界面，这个用户有没有权限。不过从另一个角度来说，这个用户不具备权限的路由，对该用户而言也不应该加载

- 动态路由：

  在router.js中

  ```js
  import store from "@/store"
  //1. 将动态载入的路由封装
  const userRule = { path:'/user',component:User }
  const roleRule = { path:'/roles',component:Roles }
  const goodRule = { path:'/goods',component:Goods }  //根据条件判断，动态添加角色相应的权限
  
  const ruleMapping={   //字符串和路由规则的映射关系
      'users':userRule,   //内部自己有的id
      'roles':roleRule,
      'goods':goodRule
  }
  {
      path:'/home',
      component:Home,
      redirect:'/welcome',
      children:[
          {
              path:'/welcome',component:Welcome
          }
      ]            
  }
  
  export function initDynamicRoutes(){
      //根据二级权限，对路由规则进行动态添加，并导出
      const currentRouter = router.options.routes  //router中options的routes下包含了路由规则
      const rightList = store.state.rightList
      rightList.forEach(item=>{
          item.children.for(item=>{
              //item:二级权限
              const temp = ruleMapping[item.path]
        		currentRouter[2].childern.push(temp)   //以一个路由/home为例，给其childre路由增加内容
          })
      })
  
      router.addRoutes(currentRouter)
  }
  ```

  在login.vue中，实现动态路由添加

  ```js
  import {initDynamicRoutes } from "@/router.js"
  
  login(){
      initDynamicRoutes()
  }
  
  //存在一个问题：当刷新时，router会丢失，其路由匹配规则也丢失了。必须返回登录页面重新登录才可以。所以在APP.vue中新增
  import {initDynamicRoutes } from "@/router.js"
  created(){
      initDynamicRoutes()
  }
  ```


##### 2.3 按钮的控制

在某个菜单的界面中， 还得根据权限数据， 展示出可进行操作的按钮，**比如删除， 修改， 增加**。可以把该逻辑放在自定义指令中

```js
//在utils.js下的premission.js中
import Vue from 'vue'
import router from "../router";
Vue.directive('premission',{
  inserted(el,binding){
    const action = binding.value.action
    //判断当前路由对应的组件中，判断用户是否具备action的权限
      console.log(router.currentRoute)   //当前了路由规则
    if(router.currentRoute.rihgtlist.indexOf(action)===-1) {// 权限列表搜寻

        if(binding.value.effect === 'disabled'){
          el.disabled = true  //禁用按钮
          el.classList.add('is-disabled')
        }else {
          el.parentNode.removeChild(el)   //删除按钮
        }
    }
  }
})

```

##### 2.4 请求和响应控制

如果用户通过非常规操作， 比如通过浏览器调试工具将某些禁用的按钮变成启用状态， 此时发的请求， 也应该被前端所拦截

**请求控制：**

- 配置请求拦截器，除了登录请求，其余的url都附带上token，这样服务器才可以鉴别身份

  ```js
  axios.interceptors.request.use(function(req){
  	const currentUrl = req.url
      if(currentUrl !==='login'){
          req.headers.Authoorization = sessionStorage.getItem('token')
      }
      return req
  })                               
  ```

- 如果发出非权限内的请求，应该直接在前端阻止，而不用发送到服务器增加其压力

  ```js
  const  actionMapping={
    'get':'view',
    'post':'add',
    'put':'edit',
    'delete':'delete'
  }
  
  axios.interceptors.request.use((req)=>{
    const currentUrl = req.url
  
    if(currentUrl !== 'login'){   //不是登录的请求，都给其赋值上token
      req.headers.Authoorization = sessionStorage.getItem('token')
      const action = actionMapping[req.method]  //当前的用户操作
      const currentRight = router.currentRoute.meta //当前路由的权限
      //判断非权限范围内请求:meta表示某一个用户的权限数据 【add,delete,edit,view】
      if(currentRight && currentRight.indexOf(action) === -1){  //权限查找，判断当前操作是否在当期路由的权限中
        //没有权限
        alert('没有权限')
        return Promise.reject(new Error('没有权限'))
      }
    }
    return req
  })
  ```

  **响应控制：**

- 得到了服务器返回的状态码401，代表token超时或者被篡改，此时应强制跳转到登录界面

  ```js
  
  ```

  

### 2. babel

### 3.响应式布局

涉及到效率问题的（比如用代码批处理解决了什么问题）

Object.definedProtry除了getter和setter还有哪些属性



对BFC的理解  https://juejin.cn/post/7061588533214969892

bable




<template>
  <div style="margin:0 50px 0 50px">
      <el-tree
      :data="data"
      node-key="id"
      
      
      draggable
      :allow-drop="allowDrop"
      :allow-drag="allowDrag">
    </el-tree>
</div>

</template>

<script>
export default {
  name:"FriendList",
  data() {
    return {
      data: [{
        id: 1,
        label: '特别关心',
        children:[{
            id: 7,
            label: '小明'
          }, 
          {
            id: 8,
            label: '小红'
          }]
      }, 
      {
        id: 2,
        label: '我的好友',
        children:[{
            id: 9,
            label: '小明'
          }, 
          {
            id: 10,
            label: '小红'
          }]
      }, 
      {
        id: 3,
        label: '朋友',
        children:[{
            id: 11,
            label: '小明'
          }, 
          {
            id: 12,
            label: '小红'
          }]
      }, 
      {
        id: 4,
        label: '家人',
        children:[{
            id: 13,
            label: '小明'
          }, 
          {
            id: 14,
            label: '小红'
          }]
      }, 
      {
        id: 5,
        label: '同学',
        children:[{
            id: 15,
            label: '小明'
          }, 
          {
            id: 16,
            label: '小红'
          }]
      }, 
      {
        id: 6,
        label: '其他',
        children:[{
            id: 17,
            label: '小明'
          }, 
          {
            id: 18,
            label: '小红'
          }]
      }, 
      
      ],
      defaultProps: {
        children: 'children',
        label: 'label'
      }
    };
  },
  methods: {
    allowDrop(draggingNode, dropNode, type) {
      if (dropNode.data.id<7) {
        return false;
      } else {
        return true;
      }
    },
    allowDrag(draggingNode) {
      // return draggingNode.data.label.indexOf('三级 3-2-2') === -1;
      return true
    }
  }

}
</script>

<style>

</style>
window.addEventListener('load',changeBtn)
function changeBtn() {
    const btnGroup = document.querySelectorAll('.btn-group')
    btnGroup.forEach(e => {
        const ul = e.querySelector('ul')
        const height = ul.offsetHeight
        const oldHeight = e.offsetHeight
        e.flag = false
        // let flag = false
        e.addEventListener('click',function () {
            e.style.transition = 'all linear .3s'
            btnGroup.forEach(e1 => {
                if (e1 !== e) {
                    e1.flag = false
                    // 此处有不足之处但无关大碍
                    e1.style.height = oldHeight + 'px'
                }
            })
            e.flag = !e.flag
            // console.log('flag',flag)
            console.log('height',height)
            console.log('oldheight',oldHeight)

            if (e.flag && height>oldHeight) {
                // console.log(1)
                e.style.height = height + oldHeight + 'px'
            }else if (!e.flag) {
                e.style.height = oldHeight + 'px'
            }
        })
    })
}
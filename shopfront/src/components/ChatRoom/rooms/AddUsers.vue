<template>
    <div>
        <select v-model="option">
            <option v-for="user in list" v-bind:key="user.id">
                {{user.attributes.username}}
            </option>
        </select>
        <mu-button class="btn-send" round color="success" @click="addUser">Добавить пользователя</mu-button>
    </div>
</template>

<script>
    export default {
        name: "AddUsers",
        props: {
            room: '',
        },
        data() {
            return {
                option: '',
                list: '',
            }
        },
        created() {
            this.loadUsers()
        },
        methods: {
            // Получаю список пользователей
            loadUsers() {
                $.ajax({
                    url: "http://127.0.0.1/main/users/",
                    type: "GET",
                    success: (response) => {
                        this.list = response.data
                    }
                })
            },
            // Добавляю пользователя в комнату
            addUser() {
                console.log(this.options)
                $.ajax({
                    url: "http://127.0.0.1/main/users/",
                    type: "POST",
                    data: {
                        room: this.room,
                        user: parseInt(this.option)
                    },
                    success: (response) => {
                        alert("Пользователь добавлен")
                    },
                    error: (response) => {
                        alert("Error add user")
                    }
                })
            }
        }
    }
</script>

<style scoped>

</style>

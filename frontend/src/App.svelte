<script>
  import { onMount } from 'svelte';
  let tasks = [];
  let newTask = '';
  let newDescription = '';

  async function getTasks() {
      const response = await fetch('http://localhost:5000/tasks');
      tasks = await response.json();
  }

  async function addTask() {
      const response = await fetch('http://localhost:5000/tasks', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ task: newTask, description: newDescription })
      });
      newTask = '';
      newDescription = '';
      getTasks();
  }

  async function updateTask(task) {
      const response = await fetch(`http://localhost:5000/tasks/${task.id}`, {
          method: 'PUT',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ completed: !task.completed })
      });
      getTasks();
  }

  async function deleteTask(task) {
      const response = await fetch(`http://localhost:5000/tasks/${task.id}`, {
          method: 'DELETE'
      });
      getTasks();
  }

  onMount(async () => {
      getTasks();
  });
</script>

<style>
  .task {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 10px;
      border-bottom: 1px solid #ccc;
  }
</style>

<h1>To-Do List</h1>

<form on:submit|preventDefault={addTask}>
  <input type="text" bind:value={newTask} placeholder="Task" />
  <input type="text" bind:value={newDescription} placeholder="Description" />
  <button type="submit">Add Task</button>
</form>

<ul>
  {#each tasks as task}
      <li class="task">
          <span>{task.task}</span>
          <span>{task.description}</span>
          <input type="checkbox" bind:checked={task.completed} on:change={() => updateTask(task)} />
          <button on:click={() => deleteTask(task)}>Delete</button>
      </li>
  {/each}
</ul>

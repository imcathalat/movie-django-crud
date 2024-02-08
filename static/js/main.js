const deleteButton = document.getElementById('deleteButton')
const deleteConfirm_modal = document.getElementById('deleteConfirm_modal')

deleteButton.addEventListener('shown.bs.modal', () => {
    deleteConfirm_modal.focus()
})

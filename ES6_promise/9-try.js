// Throw error / try catch

export default function guardrail(mathFunction) {
  const MSG = 'Guardrail was processed';
  const queue = [];
  try {
    queue.push(mathFunction());
  } catch (error) {
    queue.push(`Error: ${error.message}`);
  } finally {
    queue.push(MSG);
  }
  return queue;
}

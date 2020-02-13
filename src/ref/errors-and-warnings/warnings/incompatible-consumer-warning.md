# Incompatible Consumer Warning

<a id="helpid-30183"></a>

Message
:   `Consumer module '<module>' has incompatible dependencies. To avoid runtime errors, refresh dependencies in '<module>' and republish it.`

Cause
:   You changed a module that exposes functionality used by other module (consumer). You performed changes in the signature of exposed elements that are incompatible with the consumer module and will probably cause runtime errors.

Recommendation
:   The consumer module needs to [refresh the dependency](../../../develop/reuse-and-refactor/handle-changes.md#refresh-dependencies) to your producer module in Service Studio, adapt the logic to your changes, and be republished.

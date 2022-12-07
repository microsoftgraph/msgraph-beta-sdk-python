from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

trust_framework_key_set = lazy_import('msgraph.generated.models.trust_framework_key_set')
trust_framework_policy = lazy_import('msgraph.generated.models.trust_framework_policy')

class TrustFramework(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new TrustFramework and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The keySets property
        self._key_sets: Optional[List[trust_framework_key_set.TrustFrameworkKeySet]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The policies property
        self._policies: Optional[List[trust_framework_policy.TrustFrameworkPolicy]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TrustFramework:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TrustFramework
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TrustFramework()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "key_sets": lambda n : setattr(self, 'key_sets', n.get_collection_of_object_values(trust_framework_key_set.TrustFrameworkKeySet)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "policies": lambda n : setattr(self, 'policies', n.get_collection_of_object_values(trust_framework_policy.TrustFrameworkPolicy)),
        }
        return fields
    
    @property
    def key_sets(self,) -> Optional[List[trust_framework_key_set.TrustFrameworkKeySet]]:
        """
        Gets the keySets property value. The keySets property
        Returns: Optional[List[trust_framework_key_set.TrustFrameworkKeySet]]
        """
        return self._key_sets
    
    @key_sets.setter
    def key_sets(self,value: Optional[List[trust_framework_key_set.TrustFrameworkKeySet]] = None) -> None:
        """
        Sets the keySets property value. The keySets property
        Args:
            value: Value to set for the keySets property.
        """
        self._key_sets = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def policies(self,) -> Optional[List[trust_framework_policy.TrustFrameworkPolicy]]:
        """
        Gets the policies property value. The policies property
        Returns: Optional[List[trust_framework_policy.TrustFrameworkPolicy]]
        """
        return self._policies
    
    @policies.setter
    def policies(self,value: Optional[List[trust_framework_policy.TrustFrameworkPolicy]] = None) -> None:
        """
        Sets the policies property value. The policies property
        Args:
            value: Value to set for the policies property.
        """
        self._policies = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_object_values("keySets", self.key_sets)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("policies", self.policies)
        writer.write_additional_data_value(self.additional_data)
    


from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
terms_and_conditions = lazy_import('msgraph.generated.models.terms_and_conditions')

class TermsAndConditionsGroupAssignment(entity.Entity):
    """
    A termsAndConditionsGroupAssignment entity represents the assignment of a given Terms and Conditions (T&C) policy to a given group. Users in the group will be required to accept the terms in order to have devices enrolled into Intune.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new termsAndConditionsGroupAssignment and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Unique identifier of a group that the T&C policy is assigned to.
        self._target_group_id: Optional[str] = None
        # Navigation link to the terms and conditions that are assigned.
        self._terms_and_conditions: Optional[terms_and_conditions.TermsAndConditions] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TermsAndConditionsGroupAssignment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TermsAndConditionsGroupAssignment
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TermsAndConditionsGroupAssignment()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "target_group_id": lambda n : setattr(self, 'target_group_id', n.get_str_value()),
            "terms_and_conditions": lambda n : setattr(self, 'terms_and_conditions', n.get_object_value(terms_and_conditions.TermsAndConditions)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("targetGroupId", self.target_group_id)
        writer.write_object_value("termsAndConditions", self.terms_and_conditions)
    
    @property
    def target_group_id(self,) -> Optional[str]:
        """
        Gets the targetGroupId property value. Unique identifier of a group that the T&C policy is assigned to.
        Returns: Optional[str]
        """
        return self._target_group_id
    
    @target_group_id.setter
    def target_group_id(self,value: Optional[str] = None) -> None:
        """
        Sets the targetGroupId property value. Unique identifier of a group that the T&C policy is assigned to.
        Args:
            value: Value to set for the targetGroupId property.
        """
        self._target_group_id = value
    
    @property
    def terms_and_conditions(self,) -> Optional[terms_and_conditions.TermsAndConditions]:
        """
        Gets the termsAndConditions property value. Navigation link to the terms and conditions that are assigned.
        Returns: Optional[terms_and_conditions.TermsAndConditions]
        """
        return self._terms_and_conditions
    
    @terms_and_conditions.setter
    def terms_and_conditions(self,value: Optional[terms_and_conditions.TermsAndConditions] = None) -> None:
        """
        Sets the termsAndConditions property value. Navigation link to the terms and conditions that are assigned.
        Args:
            value: Value to set for the termsAndConditions property.
        """
        self._terms_and_conditions = value
    


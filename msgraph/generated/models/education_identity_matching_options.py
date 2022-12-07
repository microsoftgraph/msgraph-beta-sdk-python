from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

education_user_role = lazy_import('msgraph.generated.models.education_user_role')

class EducationIdentityMatchingOptions(AdditionalDataHolder, Parsable):
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
    
    @property
    def applies_to(self,) -> Optional[education_user_role.EducationUserRole]:
        """
        Gets the appliesTo property value. The appliesTo property
        Returns: Optional[education_user_role.EducationUserRole]
        """
        return self._applies_to
    
    @applies_to.setter
    def applies_to(self,value: Optional[education_user_role.EducationUserRole] = None) -> None:
        """
        Sets the appliesTo property value. The appliesTo property
        Args:
            value: Value to set for the appliesTo property.
        """
        self._applies_to = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new educationIdentityMatchingOptions and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The appliesTo property
        self._applies_to: Optional[education_user_role.EducationUserRole] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The name of the source property, which should be a field name in the source data. This property is case-sensitive.
        self._source_property_name: Optional[str] = None
        # The domain to suffix with the source property to match on the target. If provided as null, the source property will be used to match with the target property.
        self._target_domain: Optional[str] = None
        # The name of the target property, which should be a valid property in Azure AD. This property is case-sensitive.
        self._target_property_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EducationIdentityMatchingOptions:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EducationIdentityMatchingOptions
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EducationIdentityMatchingOptions()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "applies_to": lambda n : setattr(self, 'applies_to', n.get_enum_value(education_user_role.EducationUserRole)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "source_property_name": lambda n : setattr(self, 'source_property_name', n.get_str_value()),
            "target_domain": lambda n : setattr(self, 'target_domain', n.get_str_value()),
            "target_property_name": lambda n : setattr(self, 'target_property_name', n.get_str_value()),
        }
        return fields
    
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_enum_value("appliesTo", self.applies_to)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("sourcePropertyName", self.source_property_name)
        writer.write_str_value("targetDomain", self.target_domain)
        writer.write_str_value("targetPropertyName", self.target_property_name)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def source_property_name(self,) -> Optional[str]:
        """
        Gets the sourcePropertyName property value. The name of the source property, which should be a field name in the source data. This property is case-sensitive.
        Returns: Optional[str]
        """
        return self._source_property_name
    
    @source_property_name.setter
    def source_property_name(self,value: Optional[str] = None) -> None:
        """
        Sets the sourcePropertyName property value. The name of the source property, which should be a field name in the source data. This property is case-sensitive.
        Args:
            value: Value to set for the sourcePropertyName property.
        """
        self._source_property_name = value
    
    @property
    def target_domain(self,) -> Optional[str]:
        """
        Gets the targetDomain property value. The domain to suffix with the source property to match on the target. If provided as null, the source property will be used to match with the target property.
        Returns: Optional[str]
        """
        return self._target_domain
    
    @target_domain.setter
    def target_domain(self,value: Optional[str] = None) -> None:
        """
        Sets the targetDomain property value. The domain to suffix with the source property to match on the target. If provided as null, the source property will be used to match with the target property.
        Args:
            value: Value to set for the targetDomain property.
        """
        self._target_domain = value
    
    @property
    def target_property_name(self,) -> Optional[str]:
        """
        Gets the targetPropertyName property value. The name of the target property, which should be a valid property in Azure AD. This property is case-sensitive.
        Returns: Optional[str]
        """
        return self._target_property_name
    
    @target_property_name.setter
    def target_property_name(self,value: Optional[str] = None) -> None:
        """
        Sets the targetPropertyName property value. The name of the target property, which should be a valid property in Azure AD. This property is case-sensitive.
        Args:
            value: Value to set for the targetPropertyName property.
        """
        self._target_property_name = value
    


from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import education_user_role

class EducationSynchronizationLicenseAssignment(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new educationSynchronizationLicenseAssignment and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The user role type to assign to license. Possible values are: student, teacher, faculty.
        self._applies_to: Optional[education_user_role.EducationUserRole] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Represents the SKU identifiers of the licenses to assign.
        self._sku_ids: Optional[List[str]] = None
    
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
        Gets the appliesTo property value. The user role type to assign to license. Possible values are: student, teacher, faculty.
        Returns: Optional[education_user_role.EducationUserRole]
        """
        return self._applies_to
    
    @applies_to.setter
    def applies_to(self,value: Optional[education_user_role.EducationUserRole] = None) -> None:
        """
        Sets the appliesTo property value. The user role type to assign to license. Possible values are: student, teacher, faculty.
        Args:
            value: Value to set for the applies_to property.
        """
        self._applies_to = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EducationSynchronizationLicenseAssignment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EducationSynchronizationLicenseAssignment
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EducationSynchronizationLicenseAssignment()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import education_user_role

        fields: Dict[str, Callable[[Any], None]] = {
            "appliesTo": lambda n : setattr(self, 'applies_to', n.get_enum_value(education_user_role.EducationUserRole)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "skuIds": lambda n : setattr(self, 'sku_ids', n.get_collection_of_primitive_values(str)),
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
            value: Value to set for the odata_type property.
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
        writer.write_collection_of_primitive_values("skuIds", self.sku_ids)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def sku_ids(self,) -> Optional[List[str]]:
        """
        Gets the skuIds property value. Represents the SKU identifiers of the licenses to assign.
        Returns: Optional[List[str]]
        """
        return self._sku_ids
    
    @sku_ids.setter
    def sku_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the skuIds property value. Represents the SKU identifiers of the licenses to assign.
        Args:
            value: Value to set for the sku_ids property.
        """
        self._sku_ids = value
    


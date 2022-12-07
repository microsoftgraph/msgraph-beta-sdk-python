from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

layout_template_type = lazy_import('msgraph.generated.models.layout_template_type')

class LoginPageLayoutConfiguration(AdditionalDataHolder, Parsable):
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
        Instantiates a new loginPageLayoutConfiguration and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Option to show the footer on the sign-in page.
        self._is_footer_shown: Optional[bool] = None
        # Option to show the header on the sign-in page.
        self._is_header_shown: Optional[bool] = None
        # Represents the layout template to be displayed on the login page for a tenant. The possible values are  default - Represents the default Microsoft layout with a centered lightbox.  verticalSplit - Represents a layout with a backgound on the left side and a full-height lightbox to the right.  unknownFutureValue - Evolvable enumeration sentinel value. Do not use.
        self._layout_template_type: Optional[layout_template_type.LayoutTemplateType] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> LoginPageLayoutConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: LoginPageLayoutConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return LoginPageLayoutConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "is_footer_shown": lambda n : setattr(self, 'is_footer_shown', n.get_bool_value()),
            "is_header_shown": lambda n : setattr(self, 'is_header_shown', n.get_bool_value()),
            "layout_template_type": lambda n : setattr(self, 'layout_template_type', n.get_enum_value(layout_template_type.LayoutTemplateType)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def is_footer_shown(self,) -> Optional[bool]:
        """
        Gets the isFooterShown property value. Option to show the footer on the sign-in page.
        Returns: Optional[bool]
        """
        return self._is_footer_shown
    
    @is_footer_shown.setter
    def is_footer_shown(self,value: Optional[bool] = None) -> None:
        """
        Sets the isFooterShown property value. Option to show the footer on the sign-in page.
        Args:
            value: Value to set for the isFooterShown property.
        """
        self._is_footer_shown = value
    
    @property
    def is_header_shown(self,) -> Optional[bool]:
        """
        Gets the isHeaderShown property value. Option to show the header on the sign-in page.
        Returns: Optional[bool]
        """
        return self._is_header_shown
    
    @is_header_shown.setter
    def is_header_shown(self,value: Optional[bool] = None) -> None:
        """
        Sets the isHeaderShown property value. Option to show the header on the sign-in page.
        Args:
            value: Value to set for the isHeaderShown property.
        """
        self._is_header_shown = value
    
    @property
    def layout_template_type(self,) -> Optional[layout_template_type.LayoutTemplateType]:
        """
        Gets the layoutTemplateType property value. Represents the layout template to be displayed on the login page for a tenant. The possible values are  default - Represents the default Microsoft layout with a centered lightbox.  verticalSplit - Represents a layout with a backgound on the left side and a full-height lightbox to the right.  unknownFutureValue - Evolvable enumeration sentinel value. Do not use.
        Returns: Optional[layout_template_type.LayoutTemplateType]
        """
        return self._layout_template_type
    
    @layout_template_type.setter
    def layout_template_type(self,value: Optional[layout_template_type.LayoutTemplateType] = None) -> None:
        """
        Sets the layoutTemplateType property value. Represents the layout template to be displayed on the login page for a tenant. The possible values are  default - Represents the default Microsoft layout with a centered lightbox.  verticalSplit - Represents a layout with a backgound on the left side and a full-height lightbox to the right.  unknownFutureValue - Evolvable enumeration sentinel value. Do not use.
        Args:
            value: Value to set for the layoutTemplateType property.
        """
        self._layout_template_type = value
    
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
        writer.write_bool_value("isFooterShown", self.is_footer_shown)
        writer.write_bool_value("isHeaderShown", self.is_header_shown)
        writer.write_enum_value("layoutTemplateType", self.layout_template_type)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    


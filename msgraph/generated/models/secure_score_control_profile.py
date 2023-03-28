from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import compliance_information, entity, secure_score_control_state_update, security_vendor_information

from . import entity

class SecureScoreControlProfile(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new secureScoreControlProfile and sets the default values.
        """
        super().__init__()
        # Control action type (Config, Review, Behavior).
        self._action_type: Optional[str] = None
        # URL to where the control can be actioned.
        self._action_url: Optional[str] = None
        # GUID string for tenant ID.
        self._azure_tenant_id: Optional[str] = None
        # The collection of compliance information associated with secure score control
        self._compliance_information: Optional[List[compliance_information.ComplianceInformation]] = None
        # Control action category (Account, Data, Device, Apps, Infrastructure).
        self._control_category: Optional[str] = None
        # Flag to indicate where the tenant has marked a control (ignore, thirdParty, reviewed) (supports update).
        self._control_state_updates: Optional[List[secure_score_control_state_update.SecureScoreControlStateUpdate]] = None
        # Flag to indicate if a control is depreciated.
        self._deprecated: Optional[bool] = None
        # Resource cost of implemmentating control (low, moderate, high).
        self._implementation_cost: Optional[str] = None
        # The lastModifiedDateTime property
        self._last_modified_date_time: Optional[datetime] = None
        # Current obtained max score on specified date.
        self._max_score: Optional[float] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Microsoft's stack ranking of control.
        self._rank: Optional[int] = None
        # Description of what the control will help remediate.
        self._remediation: Optional[str] = None
        # Description of the impact on users of the remediation.
        self._remediation_impact: Optional[str] = None
        # Service that owns the control (Exchange, Sharepoint, Azure AD).
        self._service: Optional[str] = None
        # List of threats the control mitigates (accountBreach,dataDeletion,dataExfiltration,dataSpillage,elevationOfPrivilege,maliciousInsider,passwordCracking,phishingOrWhaling,spoofing).
        self._threats: Optional[List[str]] = None
        # Control tier (Core, Defense in Depth, Advanced.)
        self._tier: Optional[str] = None
        # Title of the control.
        self._title: Optional[str] = None
        # User impact of implementing control (low, moderate, high).
        self._user_impact: Optional[str] = None
        # The vendorInformation property
        self._vendor_information: Optional[security_vendor_information.SecurityVendorInformation] = None
    
    @property
    def action_type(self,) -> Optional[str]:
        """
        Gets the actionType property value. Control action type (Config, Review, Behavior).
        Returns: Optional[str]
        """
        return self._action_type
    
    @action_type.setter
    def action_type(self,value: Optional[str] = None) -> None:
        """
        Sets the actionType property value. Control action type (Config, Review, Behavior).
        Args:
            value: Value to set for the action_type property.
        """
        self._action_type = value
    
    @property
    def action_url(self,) -> Optional[str]:
        """
        Gets the actionUrl property value. URL to where the control can be actioned.
        Returns: Optional[str]
        """
        return self._action_url
    
    @action_url.setter
    def action_url(self,value: Optional[str] = None) -> None:
        """
        Sets the actionUrl property value. URL to where the control can be actioned.
        Args:
            value: Value to set for the action_url property.
        """
        self._action_url = value
    
    @property
    def azure_tenant_id(self,) -> Optional[str]:
        """
        Gets the azureTenantId property value. GUID string for tenant ID.
        Returns: Optional[str]
        """
        return self._azure_tenant_id
    
    @azure_tenant_id.setter
    def azure_tenant_id(self,value: Optional[str] = None) -> None:
        """
        Sets the azureTenantId property value. GUID string for tenant ID.
        Args:
            value: Value to set for the azure_tenant_id property.
        """
        self._azure_tenant_id = value
    
    @property
    def compliance_information(self,) -> Optional[List[compliance_information.ComplianceInformation]]:
        """
        Gets the complianceInformation property value. The collection of compliance information associated with secure score control
        Returns: Optional[List[compliance_information.ComplianceInformation]]
        """
        return self._compliance_information
    
    @compliance_information.setter
    def compliance_information(self,value: Optional[List[compliance_information.ComplianceInformation]] = None) -> None:
        """
        Sets the complianceInformation property value. The collection of compliance information associated with secure score control
        Args:
            value: Value to set for the compliance_information property.
        """
        self._compliance_information = value
    
    @property
    def control_category(self,) -> Optional[str]:
        """
        Gets the controlCategory property value. Control action category (Account, Data, Device, Apps, Infrastructure).
        Returns: Optional[str]
        """
        return self._control_category
    
    @control_category.setter
    def control_category(self,value: Optional[str] = None) -> None:
        """
        Sets the controlCategory property value. Control action category (Account, Data, Device, Apps, Infrastructure).
        Args:
            value: Value to set for the control_category property.
        """
        self._control_category = value
    
    @property
    def control_state_updates(self,) -> Optional[List[secure_score_control_state_update.SecureScoreControlStateUpdate]]:
        """
        Gets the controlStateUpdates property value. Flag to indicate where the tenant has marked a control (ignore, thirdParty, reviewed) (supports update).
        Returns: Optional[List[secure_score_control_state_update.SecureScoreControlStateUpdate]]
        """
        return self._control_state_updates
    
    @control_state_updates.setter
    def control_state_updates(self,value: Optional[List[secure_score_control_state_update.SecureScoreControlStateUpdate]] = None) -> None:
        """
        Sets the controlStateUpdates property value. Flag to indicate where the tenant has marked a control (ignore, thirdParty, reviewed) (supports update).
        Args:
            value: Value to set for the control_state_updates property.
        """
        self._control_state_updates = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SecureScoreControlProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SecureScoreControlProfile
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SecureScoreControlProfile()
    
    @property
    def deprecated(self,) -> Optional[bool]:
        """
        Gets the deprecated property value. Flag to indicate if a control is depreciated.
        Returns: Optional[bool]
        """
        return self._deprecated
    
    @deprecated.setter
    def deprecated(self,value: Optional[bool] = None) -> None:
        """
        Sets the deprecated property value. Flag to indicate if a control is depreciated.
        Args:
            value: Value to set for the deprecated property.
        """
        self._deprecated = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import compliance_information, entity, secure_score_control_state_update, security_vendor_information

        fields: Dict[str, Callable[[Any], None]] = {
            "actionType": lambda n : setattr(self, 'action_type', n.get_str_value()),
            "actionUrl": lambda n : setattr(self, 'action_url', n.get_str_value()),
            "azureTenantId": lambda n : setattr(self, 'azure_tenant_id', n.get_str_value()),
            "complianceInformation": lambda n : setattr(self, 'compliance_information', n.get_collection_of_object_values(compliance_information.ComplianceInformation)),
            "controlCategory": lambda n : setattr(self, 'control_category', n.get_str_value()),
            "controlStateUpdates": lambda n : setattr(self, 'control_state_updates', n.get_collection_of_object_values(secure_score_control_state_update.SecureScoreControlStateUpdate)),
            "deprecated": lambda n : setattr(self, 'deprecated', n.get_bool_value()),
            "implementationCost": lambda n : setattr(self, 'implementation_cost', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "maxScore": lambda n : setattr(self, 'max_score', n.get_float_value()),
            "rank": lambda n : setattr(self, 'rank', n.get_int_value()),
            "remediation": lambda n : setattr(self, 'remediation', n.get_str_value()),
            "remediationImpact": lambda n : setattr(self, 'remediation_impact', n.get_str_value()),
            "service": lambda n : setattr(self, 'service', n.get_str_value()),
            "threats": lambda n : setattr(self, 'threats', n.get_collection_of_primitive_values(str)),
            "tier": lambda n : setattr(self, 'tier', n.get_str_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
            "userImpact": lambda n : setattr(self, 'user_impact', n.get_str_value()),
            "vendorInformation": lambda n : setattr(self, 'vendor_information', n.get_object_value(security_vendor_information.SecurityVendorInformation)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def implementation_cost(self,) -> Optional[str]:
        """
        Gets the implementationCost property value. Resource cost of implemmentating control (low, moderate, high).
        Returns: Optional[str]
        """
        return self._implementation_cost
    
    @implementation_cost.setter
    def implementation_cost(self,value: Optional[str] = None) -> None:
        """
        Sets the implementationCost property value. Resource cost of implemmentating control (low, moderate, high).
        Args:
            value: Value to set for the implementation_cost property.
        """
        self._implementation_cost = value
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. The lastModifiedDateTime property
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. The lastModifiedDateTime property
        Args:
            value: Value to set for the last_modified_date_time property.
        """
        self._last_modified_date_time = value
    
    @property
    def max_score(self,) -> Optional[float]:
        """
        Gets the maxScore property value. Current obtained max score on specified date.
        Returns: Optional[float]
        """
        return self._max_score
    
    @max_score.setter
    def max_score(self,value: Optional[float] = None) -> None:
        """
        Sets the maxScore property value. Current obtained max score on specified date.
        Args:
            value: Value to set for the max_score property.
        """
        self._max_score = value
    
    @property
    def rank(self,) -> Optional[int]:
        """
        Gets the rank property value. Microsoft's stack ranking of control.
        Returns: Optional[int]
        """
        return self._rank
    
    @rank.setter
    def rank(self,value: Optional[int] = None) -> None:
        """
        Sets the rank property value. Microsoft's stack ranking of control.
        Args:
            value: Value to set for the rank property.
        """
        self._rank = value
    
    @property
    def remediation(self,) -> Optional[str]:
        """
        Gets the remediation property value. Description of what the control will help remediate.
        Returns: Optional[str]
        """
        return self._remediation
    
    @remediation.setter
    def remediation(self,value: Optional[str] = None) -> None:
        """
        Sets the remediation property value. Description of what the control will help remediate.
        Args:
            value: Value to set for the remediation property.
        """
        self._remediation = value
    
    @property
    def remediation_impact(self,) -> Optional[str]:
        """
        Gets the remediationImpact property value. Description of the impact on users of the remediation.
        Returns: Optional[str]
        """
        return self._remediation_impact
    
    @remediation_impact.setter
    def remediation_impact(self,value: Optional[str] = None) -> None:
        """
        Sets the remediationImpact property value. Description of the impact on users of the remediation.
        Args:
            value: Value to set for the remediation_impact property.
        """
        self._remediation_impact = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("actionType", self.action_type)
        writer.write_str_value("actionUrl", self.action_url)
        writer.write_str_value("azureTenantId", self.azure_tenant_id)
        writer.write_collection_of_object_values("complianceInformation", self.compliance_information)
        writer.write_str_value("controlCategory", self.control_category)
        writer.write_collection_of_object_values("controlStateUpdates", self.control_state_updates)
        writer.write_bool_value("deprecated", self.deprecated)
        writer.write_str_value("implementationCost", self.implementation_cost)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_float_value("maxScore", self.max_score)
        writer.write_int_value("rank", self.rank)
        writer.write_str_value("remediation", self.remediation)
        writer.write_str_value("remediationImpact", self.remediation_impact)
        writer.write_str_value("service", self.service)
        writer.write_collection_of_primitive_values("threats", self.threats)
        writer.write_str_value("tier", self.tier)
        writer.write_str_value("title", self.title)
        writer.write_str_value("userImpact", self.user_impact)
        writer.write_object_value("vendorInformation", self.vendor_information)
    
    @property
    def service(self,) -> Optional[str]:
        """
        Gets the service property value. Service that owns the control (Exchange, Sharepoint, Azure AD).
        Returns: Optional[str]
        """
        return self._service
    
    @service.setter
    def service(self,value: Optional[str] = None) -> None:
        """
        Sets the service property value. Service that owns the control (Exchange, Sharepoint, Azure AD).
        Args:
            value: Value to set for the service property.
        """
        self._service = value
    
    @property
    def threats(self,) -> Optional[List[str]]:
        """
        Gets the threats property value. List of threats the control mitigates (accountBreach,dataDeletion,dataExfiltration,dataSpillage,elevationOfPrivilege,maliciousInsider,passwordCracking,phishingOrWhaling,spoofing).
        Returns: Optional[List[str]]
        """
        return self._threats
    
    @threats.setter
    def threats(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the threats property value. List of threats the control mitigates (accountBreach,dataDeletion,dataExfiltration,dataSpillage,elevationOfPrivilege,maliciousInsider,passwordCracking,phishingOrWhaling,spoofing).
        Args:
            value: Value to set for the threats property.
        """
        self._threats = value
    
    @property
    def tier(self,) -> Optional[str]:
        """
        Gets the tier property value. Control tier (Core, Defense in Depth, Advanced.)
        Returns: Optional[str]
        """
        return self._tier
    
    @tier.setter
    def tier(self,value: Optional[str] = None) -> None:
        """
        Sets the tier property value. Control tier (Core, Defense in Depth, Advanced.)
        Args:
            value: Value to set for the tier property.
        """
        self._tier = value
    
    @property
    def title(self,) -> Optional[str]:
        """
        Gets the title property value. Title of the control.
        Returns: Optional[str]
        """
        return self._title
    
    @title.setter
    def title(self,value: Optional[str] = None) -> None:
        """
        Sets the title property value. Title of the control.
        Args:
            value: Value to set for the title property.
        """
        self._title = value
    
    @property
    def user_impact(self,) -> Optional[str]:
        """
        Gets the userImpact property value. User impact of implementing control (low, moderate, high).
        Returns: Optional[str]
        """
        return self._user_impact
    
    @user_impact.setter
    def user_impact(self,value: Optional[str] = None) -> None:
        """
        Sets the userImpact property value. User impact of implementing control (low, moderate, high).
        Args:
            value: Value to set for the user_impact property.
        """
        self._user_impact = value
    
    @property
    def vendor_information(self,) -> Optional[security_vendor_information.SecurityVendorInformation]:
        """
        Gets the vendorInformation property value. The vendorInformation property
        Returns: Optional[security_vendor_information.SecurityVendorInformation]
        """
        return self._vendor_information
    
    @vendor_information.setter
    def vendor_information(self,value: Optional[security_vendor_information.SecurityVendorInformation] = None) -> None:
        """
        Sets the vendorInformation property value. The vendorInformation property
        Args:
            value: Value to set for the vendor_information property.
        """
        self._vendor_information = value
    

